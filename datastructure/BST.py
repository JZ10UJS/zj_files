from .tree import BinTree


class BinarySearchTree(BinTree):
    def _search(self, val):
        node = self.root
        _hot = None
        while 1:
            if not node or node.data == val:
                return node, _hot

            _hot = node
            if node.data < val:
                node = node.right
            else:
                node = node.left

    def search(self, val):
        node, _hot = self._search(val)
        return node

    def insert(self, val):
        node, _hot = self._search(val)
        if node:
            r = node
        elif _hot.data < val:
            r = self._insert_as_right(_hot, val)
        else:
            r = self._insert_as_left(_hot, val)
        return r

    def remove(self, val):
        node, _hot = self._search(val)
        if not node:
            return
        self.remove_at(node, _hot)
