"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        #for i in range(len(root.children)):
        if root == None: return 0
        if not root.children: return 1
        return 1+ max([self.maxDepth(child) for child in root.children])