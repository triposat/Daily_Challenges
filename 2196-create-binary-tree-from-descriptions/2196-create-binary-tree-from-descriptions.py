# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, res: List[List[int]]) -> Optional[TreeNode]:
        hMap = {}
        child = set()
        parent = set()
        for par, chl, d in res:
            node = hMap.setdefault(par, TreeNode(par))
            node1 = hMap.setdefault(chl, TreeNode(chl))
            if d:
                node.left = node1
            else:
                node.right = node1
            child.add(chl)
            parent.add(par)
        root = (parent-child).pop()
        return hMap[root]