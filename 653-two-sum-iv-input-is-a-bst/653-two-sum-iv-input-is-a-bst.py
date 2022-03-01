# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []

        def solve(root):
            if root:
                solve(root.left)
                res.append(root.val)
                solve(root.right)
        solve(root)
        hashMap = {}
        for idx, val in enumerate(res):
            rem = k-res[idx]
            if rem in hashMap:
                return True
            hashMap[val] = idx
        return False