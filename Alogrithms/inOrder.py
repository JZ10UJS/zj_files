#!usr/bin/python
# coding:utf-8

"""
----------
有真二叉的先序和后序，return中序
----------
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class binTree(object):
    def __init__(self,root):
        self.root = root


def gouzaobt(prenums, postnums):
    if len(prenums) == 1:
        return prenums
    
    root = TreeNode(prenums[0])
    root.left.val = prenums[1]
    root.right.val = postnums[-2]
    
