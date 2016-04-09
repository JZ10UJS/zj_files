#!/usr/bin/python
# coding: utf-8


import re
import unittest


class CodeBuilder(object):
    def __init__(self, indent=0):
        self.code = []
        self.indent_level = indent

    def add_line(self, line):
        self.code.extend([" " * self.indent_level, line, "\n"])

    def add_section(self):
        # 主要是为了占个位置，方便后面添加其他代码上来。
        section = CodeBuilder(self.indent_level)
        self.code.append(section)
        return section

    def __str__(self):
        """self.code中可能还有CodeBuilder的实例，所以需要递归的处理"""
        return ''.join(str(c) for c in self.code)

    def indent(self):
        self.indent_level += 4

    def dedent(self):
        self.indent_level -= 4

    def get_globals(self):
        assert self.indent_level == 0
        globals_name = {}
        exec(str(self), globals_name)
        return globals_name


class Template(object):
    def __init__(self, text, *contexts):
        self.context = {}
        for context in contexts:
            if context:
                self.context.update(context)

        # 存放模板中的所有变量名字, for循环中的循环变量也加入
        self.all_vars = set()

        code = CodeBuilder()
        code.add_line('def render_function(context, do_dots):')     
        code.indent()
        
        # 占位置，当处理到后面，且知道模板变量名字时，用以赋值。
        vars_code = code.add_section()

        code.add_line('result = []')
        # 方便Python迅速查找
        code.add_line('append_result = result.append')
        code.add_line('extend_result = result.extend')
        code.add_line('to_str = str')

        # buffered中的有些数据得经过 repr()处理
        # 否则 在 code中 就变成了 append_result(<html>)
        # 而不是 append_result('<html>')
        buffered = []
        def flush_output():
            if len(buffered) == 1:
                code.add_line('append_result(%s)' % buffered[0])
            if len(buffered) > 1:
                code.add_line('extend_result([%s])' % ', '.join(buffered))
            del buffered[:]

        ops_stack = []
        tokens = re.split(r'(?s)({{.*?}}|{%.*?%}|{#.*?#})', text)

        for token in tokens:
            if token.startswith('{#'):
                continue
            elif token.startswith('{{'):
                expr = token[2:-2].strip()
                expr = self._expr_code(expr)
                # 加到buffered的是表达式，在code中实际生成的就是
                # append_result(to_str(c_name))
                # extend_result(["<html>", to_str(...), ..])
                buffered.append('to_str(%s)' % expr)
            elif token.startswith('{%'):
                # 这种情况，就需要先清空buffered
                flush_output()
                words = token[2:-2].strip().split()
                if words[0] == 'if':
                    if len(words) != 2:
                        self._syntax_error('Do not understand if', token)
                    ops_stack.append('if')
                    expr = self._variable(words[1], self.all_vars)
                    code.add_line('if %s:' % expr)
                    code.indent()
                elif words[0] == 'else':
                    if len(words) != 1:
                        self._syntax_error('Do not understand else', token)
                    code.dedent()
                    code.add_line('else:')
                    code.indent()
                elif words[0] == 'for':
                    if len(words) != 4 or words[2] != 'in':
                        self._syntax_error('Do not understand for', token)
                    ops_stack.append('for')
                    # 将for循环的变量 加入到 self.loop_vars 中
                    # 因为是循环变量，所以不用改为 'c_%s' 形式，不用重新赋值
                    loop_name = self._variable(words[1], self.all_vars)
                    # 被循环的 则需要改名字，并加入self.all_vars中
                    var_name = self._variable(words[3], self.all_vars)
                    code.add_line('for %s in %s:' % (loop_name, var_name))
                    code.indent()
                elif words[0].startswith('end'):
                    if len(words) != 1:
                        self._syntax_error('To many items in end.', token)
                    end_what = words[0][3:]
                    if not ops_stack:
                        self._syntax_error('To many end', token)
                    start_what = ops_stack.pop()
                    if start_what != end_what:
                        self._syntax_error('Miss matched tag', token)
                    code.dedent()
                else:
                    self._syntax_error('Do not understand tag', token)
                    
            else:
                if token:
                    buffered.append(repr(token))
                    
        flush_output()

        if len(ops_stack) != 0:
            self._syntax_error('There still has some ops left.', ops_stack)

        # 在token处理完成之后，模板中的变量都被存到了 self.all_vars中
        for var_name in self.all_vars:
            # 给函数中的context中的变量加个c_开头，避免混淆，
            # 为了防止传入的context中没有模板中的某些变量，加个try语句，
            vars_code.add_line('try:')
            vars_code.indent()
            vars_code.add_line('c_%s = context[%r]' % (var_name, var_name))
            vars_code.dedent()
            vars_code.add_line('except KeyError:')
            vars_code.indent()
            vars_code.add_line('c_%s = %r' % (var_name, ''))
            vars_code.dedent()

        code.add_line('return "".join(result)')
        code.dedent()
        self._render_function = code.get_globals()['render_function']
        

    def _expr_code(self, expr):
        if '.' in expr:
            dots = expr.split('.')
            code = self._variable(dots[0], self.all_vars)
            # 为了传入之后是 do_dots(x, 'y', 'z') 而不是do_dots(x, y, z)
            args = ', '.join(repr(arg) for arg in dots[1:])
            code = "do_dots(%s, %s)" % (code, args)
        elif '|' in expr:
            pipes = expr.split('|')
            code = self._variable(pipes[0], self.all_vars)
            for func in pipes[1:]:
                func = self._variable(func, self.all_vars)
                code = "%s(%s)" % (func, code)
        else:
            code = self._variable(expr, self.all_vars)
        return code

    def _variable(self, name, vars_set):
        "检查一下名字是否合法，然后加入变量集合中，最后加个前缀，避免混淆"
        if not re.match(r"[_a-zA-Z][0-9A-Za-z]*", name):
            self._syntax_error('Not a valid name', name)
        vars_set.add(name)
        return 'c_%s' % name

    def _do_dots(self, value, *dots):
        for dot in dots:
            try:
                value = getattr(value, dot)
            except AttributeError:
                value = value[dot]
            if callable(value):
                value = value()
        return value

    def render(self, context=None):
        render_context = dict(self.context)
        if context:
            render_context.update(context)
        return self._render_function(render_context, self._do_dots)

    def _syntax_error(self, msg, thing):
        raise TempalteSyntaxError(msg, thing)


class TempalteSyntaxError(ValueError):
    pass
            

class CodeBuilderTest(unittest.TestCase):
    def setUp(self):
        self.code = CodeBuilder()
        self.vars_code = self.code.add_section()
        self.code.add_line('def foo():')
        self.code.indent()
        self.code.add_line('return x+y')
        self.code.dedent()

    def test_ans(self):
        self.vars_code.add_line('x = 2')
        self.vars_code.add_line('y = 14')
        my_foo = self.code.get_globals()['foo']
        self.assertEqual(my_foo(), 16)
        

class TemplateTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_normal(self):
        text = '<html>\nhello, \n  </body>\n</html>'
        self.t = Template(text)
        c = {'name':'zhangjie'}
        r_ans = '<html>\nhello, \n  </body>\n</html>'
        res = self.t.render(c)
        self.assertEqual(res, r_ans)

    def test_pipe(self):
        text = '{{name|foo|bar}} hahah info'
        t = Template(text)
        c = {
            'foo': lambda x: 'Hello, ' + x,
            'name': 'zhangjie',
            'bar': lambda x: x+', what the fuck'
        }
        r_ans = 'Hello, zhangjie, what the fuck hahah info'
        self.assertEqual(t.render(c), r_ans)

    def test_dot(self):
        text = 'hello {{name.upper}}, haha<html>{{name.lower}},{{name.lower.capitalize}}'
        t = Template(text)
        c = {'name': 'zhangjie'}
        r_ans = 'hello ZHANGJIE, haha<html>zhangjie,Zhangjie'
        self.assertEqual(t.render(c), r_ans)

    def test_if(self):
        text = '{%if ab%}h{%else%}H{%endif%}ello, {% if name %}{{name.upper}}{% endif %}'
        t = Template(text)
        c = {'name': 'zhangjie'}
        r_ans = 'Hello, ZHANGJIE'
        self.assertEqual(t.render(c), r_ans)

    def test_for(self):
        text = 'Hello, {% for letter in name %}{{letter.upper}}\n{% endfor %}'
        t = Template(text)
        c = {'name': 'zhangjie'}
        r_ans = 'Hello, Z\nH\nA\nN\nG\nJ\nI\nE\n'
        self.assertEqual(t.render(c), r_ans)


if __name__ == '__main__':
    unittest.main()
    

    
