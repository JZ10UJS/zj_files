from .BST import BinarySearchTree


def stature(node):
    if node is None:
        return -1
    return node.height


class AVL(BinarySearchTree):
    @staticmethod
    def balanced(node):
        return stature(node.left) == stature(node.right)

    @staticmethod
    def bal_fac(node):
        return stature(node.left) - stature(node.right)

    @staticmethod
    def avl_balanced(node):
        return -1 <= AVL.bal_fac(node) <= 1

    @staticmethod
    def taller_child(node):
        if stature(node.left) > stature(node.right):
            return node.left
        elif stature(node.left) < stature(node.right):
            return node.right
        elif node.parent.left is node:
            return node.left
        else:
            return node.right

    def rotate_at(self, v):
        p, g = v.parent, v.parent.parent
        if g.left is p:
            if p.left is v:
                p.parent = g.parent
                return AVL.connect_34(v, p, g, v.left, v.right, p.right, g.right)
            else:
                v.parent = g.parent
                return AVL.connect_34(p, v, g, p.left, v.left, v.right, g.right)
        else:
            if p.right is v:
                p.parent = g.parent
                return AVL.connect_34(g, p, v, g.left, p.left, v.left, v.right)
            else:
                v.parent = g.parent
                return AVL.connect_34(g, v, p, g.left, v.left, v.right, p.right)

    @staticmethod
    def connect_34(a, b, c, t0, t1, t2, t3):
        a.left = t0
        if t0:
            t0.parent = a
        a.right = t1
        if t1:
            t1.parent = a

        c.left = t2
        if t2:
            t2.parent = c
        c.right = t3
        if t3:
            t3.parent = c

        b.left, a.parent = a, b
        b.right, c.parent = c, b
        return b

    def insert(self, val):
        node, _hot = self._search(val)
        if node:
            return node

        # 不调用tree的insert_as_*，避免更新全部祖先的height
        if _hot.data < val:
            r = _hot._insert_as_right(val)
        else:
            r = _hot._insert_as_left(val)
        self._size += 1
        g = r.parent
        while g:
            if not self.avl_balanced(g):
                # find the first ancestor which is not avl balanced
                # handle it and break;
                self.rotate_at(self.taller_child(self.taller_child(g)))
                self._update_height(g)
                break
            else:
                # 此时更新祖先的height
                self._update_height(g)
            g = g.parent
        return r

    def remove(self, val):
        node, _hot = self._search(val)
        if not node:
            return False
        self.remove_at(node, _hot, _update_height=False)
        while _hot:
            if not self.avl_balanced(_hot):
                self.rotate_at(self.taller_child(self.taller_child(_hot)))
            self._update_height(_hot)
            _hot = _hot.parent
        return True
