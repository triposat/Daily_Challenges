# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        while root:
            if root.val in range(p.val, q.val+1) or root.val in range(q.val, p.val+1):
                return root
            if root.val < p.val:
                root = root.right
            else:
                root = root.left