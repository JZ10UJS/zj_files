from .tree import BinNode
from .BST import BinarySearchTree


class SplayTree(BinarySearchTree):
    """
    伸展树
    """
    @staticmethod
    def _attach_as_left_child(n1, n2):
        n1.left = n1
        if n2:
            n2.parent = n1

    @staticmethod
    def _attach_as_right_child(n1, n2):
        n1.right = n2
        if n2:
            n2.parent = n1

    def _splay(self, node):
        """
        将node节点伸展至根
        :param node:
        :return:
        """
        if not node:
            return

        while node.parent and node.parent.parent:
            p, g = node.parent, node.parent.parent
            gg = g.parent
            if p.left is node:
                if g.left is p:     # zig-zig
                    self._attach_as_left_child(g, p.right)
                    self._attach_as_left_child(p, node.right)
                    self._attach_as_right_child(p, g)
                    self._attach_as_right_child(node, p)
                else:               # zig-zag
                    self._attach_as_right_child(g, node.left)
                    self._attach_as_left_child(p, node.right)
                    self._attach_as_left_child(node, g)
                    self._attach_as_right_child(node, p)
            else:
                if g.right is p:    # zag-zag
                    self._attach_as_right_child(g, p.left)
                    self._attach_as_right_child(p, node.left)
                    self._attach_as_left_child(p, g)
                    self._attach_as_left_child(node, p)
                else:               # zag-zig
                    self._attach_as_left_child(g, node.right)
                    self._attach_as_right_child(p, node.left)
                    self._attach_as_left_child(node, p)
                    self._attach_as_right_child(node, g)
            if not gg:
                node.parent = None
            else:
                if gg.left is g:
                    self._attach_as_left_child(gg, node)
                else:
                    self._attach_as_right_child(gg, node)
            self._update_height(g)
            self._update_height(p)
            self._update_height(node)

        # 此时node还有parent就是 while 循环被 node.parent.parent break;
        if node.parent:
            p = node.parent
            if p.left is node:
                self._attach_as_left_child(p, node.right)
                self._attach_as_right_child(node, p)
            else:
                self._attach_as_right_child(p, node.left)
                self._attach_as_left_child(node, p)
        # node变为树根， parent指向None
        node.parent = None
        self._root = node
        return node

    def search(self, val):
        node, _hot = self._search(val)
        if node:
            self._splay(node)
        else:
            self._splay(_hot)
        return self._root

    def insert(self, val):
        hot = self.search(val)
        if hot.data == val:
            return hot
        else:
            node = BinNode(val)
            if hot.data < val:
                self._attach_as_right_child(node, hot.right)
                self._attach_as_left_child(node, hot)
            else:
                self._attach_as_left_child(node, hot.left)
                self._attach_as_right_child(node, hot)
            self._root = node
            return node

    def remove(self, val) -> bool:
        hot = self.search(val)
        if hot.data != val:
            return False
        else:
            # 找到hot节点中序遍历直接后继， 替换二者的值，然后移除succ节点
            succ = hot.succ()
            r, parent = succ.right, succ.parent
            self.swap_node_data(hot, succ)
            if parent is hot:
                parent.right = r
            else:
                parent.left = r
            if r:
                r.parent = hot
            return True
