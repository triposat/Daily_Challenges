# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not t1:
            return t2
        if not t2:
            return t1
        def solve(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1
            res = TreeNode(t1.val+t2.val)
            res.left = solve(t1.left, t2.left)
            res.right = solve(t1.right, t2.right)
            return res
        
        return solve(t1, t2)
        