import unittest
from .tree import BinNode, BinTree, node_height
from .BST import BinarySearchTree
from .AVL import AVL


class NodeTest(unittest.TestCase):
    def test_001_no_child_node_height(self):
        node = BinNode(14)
        self.assertEqual(node.height, 0)
        self.assertEqual(node_height(node.left), -1)
        self.assertEqual(node_height(None), -1)


class BinTreeNodeTest(unittest.TestCase):
    """
                 14
            6        20
        4      10
    2
    """
    def setUp(self):
        self.r = node = BinNode(14)
        self.t = t = BinTree(node)
        t._insert_as_left(node, 6)
        t._insert_as_right(node, 20)
        t._insert_as_left(node.left, 4)
        t._insert_as_right(node.left, 10)
        t._insert_as_right(node.left.left, 2)
        return node, t

    def test_002_2_child_height(self):
        node = self.r
        self.assertEqual(node.left.left.height, 1)
        self.assertEqual(node.left.height, 2)
        self.assertEqual(node.height, 3)
        self.assertEqual(node.right.height, 0)

    def test_none_tree(self):
        t = BinTree(None)
        self.assertTrue(t.empty() is True)
        t = BinTree(BinNode(12))
        self.assertEqual(t.size, 1)
        node = BinNode(12)
        node._insert_as_right(BinNode(20))
        node.right._insert_as_left(BinNode(13))
        self.assertEqual(node.size(), 3)

    def test_006_travel_pre(self):
        node = BinNode(14)
        t = BinTree(node)
        t._insert_as_left(node, 12)
        t._insert_as_right(node, 13)
        t._insert_as_left(node.left, 14)
        t._insert_as_right(node.left.left, 14)
        l = []
        t.travel_pre_recursive(node, visit=l.append)
        l2 = []
        t.travel_pre_v1(node, visit=l2.append)
        l3 = []
        t.travel_pre_v2(node, visit=l3.append)
        self.assertTrue(l == l2 == l3)

    def test_007_travel_in(self):
        node, t = self.r, self.t
        l = []
        t.travel_in_v1(node, visit=l.append)
        l2 = []
        t.travel_in(node, visit=l2.append)
        self.assertTrue(l == l2)

    def test_007_travel_post(self):
        node, t = self.r, self.t
        l = []
        t.travel_post_v1(node, visit=l.append)
        self.assertEqual(l, [2, 4, 10, 6, 20, 14])


class BSTTestCase(unittest.TestCase):
    """
                14
        10           15
    6      13              19
                        17      28
    """
    def setUp(self):
        r = self.r = BinNode(14)
        t = self.t = BinarySearchTree(r)
        v = [10, 15, 13, 6, 19, 17, 28]
        for i in v:
            t.insert(i)

    def test_001_search(self):
        self.assertEqual(self.t.search(6).data, 6)
        self.assertEqual(self.t.search(14), self.r)
        self.assertEqual(self.t.search(10).data, 10)
        self.assertTrue(self.t.search(10) is self.r.left)
        self.assertTrue(self.t.search(20) is None)

    def test_002_insert(self):
        node = self.t.insert(11)
        self.assertTrue(self.r.left.right.left is node)
        node = self.t.insert(16)
        self.assertTrue(self.r.right.right.left.left is node)
        self.assertEqual(self.r.right.right.left.left.data, 16)
        node = self.t.insert(13)
        self.assertTrue(node is self.t.search(13))

    def test_003_remove_node_only_have_r_child(self):
        self.t.remove(15)
        self.assertTrue(self.r.right is self.t.search(19))
        self.assertEqual(self.r.height, 2)
        l = []
        self.t.travel_in(self.r, visit=lambda x: l.append(x))
        self.assertEqual(l, [6, 10, 13, 14, 17, 19, 28])

    def test_004_remove_node_only_have_l_child(self):
        self.t.insert(4)
        self.assertEqual(self.r.height, 3)
        self.assertEqual(self.r.left.height, 2)
        self.t.remove(6)
        self.assertTrue(self.r.left.left is self.t.search(4))
        self.assertEqual(self.r.left.height, 1)
        l = []
        self.t.travel_in(self.r, visit=lambda x: l.append(x))
        self.assertEqual(l, [4, 10, 13, 14, 15, 17, 19, 28])

    def test_005_remove_node_have_both_child(self):
        node = self.t.insert(11)
        node_10 = self.t.search(10)
        self.assertTrue(self.r.left.right.left is node)
        self.t.remove(10)
        self.assertEqual(self.r.left.data, 11)
        new_node_11 = self.t.search(11)
        self.assertTrue(new_node_11 is not node)
        self.assertTrue(new_node_11 is node_10)
        self.assertTrue(new_node_11.parent is self.r)
        self.assertTrue(self.r.left is new_node_11)
        self.assertTrue(self.t.search(6).parent is new_node_11)
        self.assertTrue(new_node_11.left is self.t.search(6))
        self.assertTrue(self.t.search(13).parent is new_node_11)
        self.assertTrue(new_node_11.right is self.t.search(13))
        l = []
        self.t.travel_in(self.r, visit=lambda x: l.append(x))
        self.assertEqual(l, [6, 11, 13, 14, 15, 17, 19, 28])

    def test_006_remove_node_have_bchild_2(self):
        self.t.insert(30)
        self.t.remove(19)
        self.assertTrue(self.t.search(28).left is self.t.search(17))
        self.assertTrue(self.t.search(28).right is self.t.search(30))
        l = []
        self.t.travel_in(self.r, visit=lambda x: l.append(x))
        self.assertEqual(l, [6, 10, 13, 14, 15, 17, 28, 30])

    def test_007_remove_node_not_exists(self):
        l = []
        self.t.travel_in(self.r, visit=lambda x: l.append(x))
        res = self.t.remove(199)
        self.assertTrue(res is None)
        l1 = []
        self.t.travel_in(self.r, visit=lambda x: l1.append(x))
        self.assertEqual(l, l1)


class AVLTest(unittest.TestCase):
    """
                      20
               10              50
           5        15    30      99
        3    6   14         35
     2
    """
    def setUp(self):
        self.basic = [2, 3, 5, 6, 10, 14, 15, 20, 30, 35, 50, 99]
        r = self.r = BinNode(20)
        t = self.t = AVL(self.r)
        t._insert_as_left(r, 10)
        t._insert_as_right(r, 50)
        t._insert_as_left(r.left, 5)
        t._insert_as_right(r.left, 15)
        t._insert_as_left(r.right, 30)
        t._insert_as_right(r.right, 99)
        t._insert_as_left(t.search(5), 3)
        t._insert_as_right(t.search(5), 6)
        t._insert_as_left(t.search(3), 2)
        t._insert_as_left(t.search(15), 14)
        t._insert_as_right(t.search(30), 35)

    def test_001_in_order(self):
        self.assertEqual(self.t.get_in_order(), self.basic)

    def test_002_insert_with_avl_balanced(self):
        t = self.t
        n99 = t.search(99)
        self.assertEqual(n99.height, 0)
        node = t.insert(100)
        self.assertTrue(t.search(99).right is node)
        self.assertTrue(node.parent is t.search(99))
        self.assertEqual(self.t.get_in_order(), self.basic + [100])
        self.assertEqual(n99.height, 1)

    def test_003_insert_with_all_left(self):
        t = self.t
        n2, n3 = t.search(2), t.search(3)
        self.assertEqual(n2.height, 0)
        self.assertEqual(n3.height, 1)
        n1 = t.insert(1)
        self.assertTrue(n1.parent is n2)
        self.assertTrue(n2.left is n1)
        self.assertTrue(n2.right is n3)
        self.assertTrue(n3.parent is n2)
        self.assertTrue(n2.parent is t.search(5))
        self.assertEqual(n2.height, 1)
        self.assertEqual(n3.height, 0)
        self.assertEqual(t.search(5).height, 2)


if __name__ == '__main__':
    unittest.main()
