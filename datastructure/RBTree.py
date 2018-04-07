from .BST import BinarySearchTree
from .tree import BinNode


def stature(node):
    if node is None:
        return 0
    return node.height


class RedBlackNode(BinNode):
    def __init__(self, data, is_black=True, parent=None, left=None, right=None):
        super().__init__(data, parent=parent, left=left, right=right)
        self.is_black = is_black


class RedBlackTree(BinarySearchTree):
    """
    统一增设外部节点None, 使之成为真二叉树
    树根: 必须为黑色
    外部节点: 均为黑色
    其余节点: 若为红，只能有黑色孩子         // 红之子，红之父必为黑
    外部节点到根节点: 途中黑色节点数目相等    // 黑深度
    """

    def _solve_double_red(self, node):
        pass

    def _solve_double_black(self, node):
        pass

    def _update_height(self, node):
        """此时节点高度为，黑高度"""
        node.height = max(stature(node.left), stature(node.right))
        if node.is_black:
            node.height += 1
        return node.height

    def insert(self, val):
        v, _hot = self._search(val)
        if v:
            return False
        if _hot.data < val:
            v = _hot._insert_as_right(val)
        else:
            v = _hot._insert_as_left(val)
        self._size += 1
        v.is_black = False
        if _hot.is_black:
            return v
        else:
            self._solve_double_red(v)

    def remove(self, val):
        pass
