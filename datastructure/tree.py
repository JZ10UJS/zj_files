

class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0

    def size(self):
        raise NotImplementedError


def node_height(node):
    if node is None:
        return -1
    return node.height


class BinNode(Node):
    def __init__(self, data, parent=None, left=None, right=None):
        super().__init__(data)
        self.parent = parent
        self.left = left
        self.right = right

    def _insert_as_left(self, val):
        node = self.left = self.__class__(val, parent=self)
        return node

    def _insert_as_right(self, val):
        node = self.right = self.__class__(val, parent=self)
        return node

    def size(self):
        """return the nodes count include it self"""
        s = 1
        if self.left:
            s += self.left.size()
        if self.right:
            s += self.right.size()
        return s

    def succ(self):
        """
        :return: BinNode or None
        """
        n = self.right
        if n:
            while n.left:
                n = n.left
        return n

    def __repr__(self):
        return 'BinNode<%s>' % self.data


class BinTree:
    def __init__(self, root):
        self._size = 1
        self._root = root

    def _update_height(self, node):
        """
        update the height of this node
        :param node:
        :return:
        """
        res = node.height = max(node_height(node.left), node_height(node.right)) + 1
        return res

    def __update_height_above(self, node):
        """
        update the height of this node, so to it's parents
        :param node:
        :return:
        """
        while node:
            self._update_height(node)
            node = node.parent

    @property
    def size(self):
        return self._size

    def empty(self):
        return not self._root

    @property
    def root(self):
        return self._root

    def _insert_as_right(self, node, val):
        self._size += 1
        node._insert_as_right(val)
        self.__update_height_above(node)
        return node.right

    def _insert_as_left(self, node, val):
        self._size += 1
        node._insert_as_left(val)
        self.__update_height_above(node)
        return node.left

    def remove_at(self, child, parent, _update_height=True):
        relation = 'left' if parent.left is child else 'right'
        if child.left is None:
            setattr(parent, relation, child.right)
            succ = child.right
        elif child.right is None:
            setattr(parent, relation, child.left)
            succ = child.left
        else:
            w = child.succ()
            succ, parent = w.right, w.parent
            self.swap_node_data(child, w)
            if parent is child:
                parent.right = succ
            else:
                parent.left = succ
        if succ:
            succ.parent = parent
        if _update_height:
            self.__update_height_above(parent)
        self._size -= 1
        return succ

    def swap_node_data(self, n1, n2):
        n1.data, n2.data = n2.data, n1.data

    @staticmethod
    def travel_pre_v1(node, visit):
        stack = [node]
        while stack:
            n = stack.pop()
            visit(n.data)
            if n.right:
                stack.append(n.right)
            if n.left:
                stack.append(n.left)

    @staticmethod
    def visit_along_left_branch(node, visit, stack):
        while node:
            visit(node.data)
            stack.append(node.right)
            node = node.left

    @classmethod
    def travel_pre_v2(cls, node, visit):
        s = []
        while 1:
            cls.visit_along_left_branch(node, visit, s)
            if not s:
                break
            node = s.pop()

    @classmethod
    def travel_pre_recursive(cls, node, visit):
        """

        :param node: BinNode
        :param visit: function
        :return: None
        """
        if not node:
            return
        visit(node.data)
        cls.travel_pre_recursive(node.left, visit)
        cls.travel_pre_recursive(node.right, visit)

    def travel_in_v1(self, node=None, visit=print):
        if not node:
            return
        self.travel_in_v1(node.left, visit)
        visit(node.data)
        self.travel_in_v1(node.right, visit)

    @staticmethod
    def go_along_left_branch(node, s):
        while node:
            s.append(node)
            node = node.left

    @classmethod
    def travel_in(cls, node, visit):
        s = []
        while 1:
            cls.go_along_left_branch(node, s)
            if not s:
                break
            node = s.pop()
            visit(node.data)
            node = node.right

    def travel_post_v1(self, node, visit):
        if not node:
            return
        self.travel_post_v1(node.left, visit)
        self.travel_post_v1(node.right, visit)
        visit(node.data)

    def travel_post(self, node, visit):
        pass

    def get_in_order(self):
        l = []
        self.travel_in(self.root, visit=l.append)
        return l
