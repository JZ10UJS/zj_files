def _find_idx(l, d):
    """
    返回l中，不大于d的最大的那个index
    :param l:
    :param d:
    :return:
    """
    idx = len(l) - 1
    while idx > -1:
        if l[idx] <= d:
            return idx
        idx -= 1
    return idx


class BTNode:
    def __init__(self, e, lc=None, rc=None, parent=None):
        self.keys = [e]
        self.childrens = [lc, rc]
        self.parent = parent
        if lc:
            lc.parent = self
        if rc:
            rc.parent = self


class BTree:
    def __init__(self, root):
        self._order = None
        self._root = root
        self._size = 1

    def _solve_overflow(self, v):
        """
        插入而上溢后的分裂处理
        :return:
        """
        pass

    def _solve_underflow(self, v):
        """
        删除而下溢后的合并处理
        :return:
        """
        pass

    def _search(self, e) -> (BTNode, BTNode):
        v, _hot = self._root, None
        while v:
            r = _find_idx(v.keys, e)
            if r >= 0 and v.keys[r] == e:
                return v, _hot
            _hot, v = v, v.childrens[r+1]
        return None, _hot

    def search(self, e) -> BTNode:
        v, _hot = self._search(e)
        return v

    def insert(self, e) -> bool:
        v, _hot = self._search(e)
        if v:
            return False
        r = _find_idx(_hot.keys, e)
        _hot.keys.insert(r+1, e)
        _hot.childrens.append(None)
        self._size += 1
        self._solve_overflow(_hot)
        return True

    def remove(self, e) -> bool:
        v = self.search(e)
        if not v:
            return False
        r = _find_idx(v.keys, e)
        if v.childrens[0] is not None:
            # 如果 v 不是叶子节点，就让 v 与其直接后继互换值
            u = v.childrens[r+1]
            while u.childlrens[0]:
                u = u.childlrens[0]
            v.keys[r] = u.keys[0]
            v, r = u, 0
        v.keys.pop(r)
        v.childrens.pop()
        self._size -= 1
        self._solve_underflow(v)
        return True
