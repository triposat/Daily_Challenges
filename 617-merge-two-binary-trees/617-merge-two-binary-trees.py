# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def solve(n, to):
#     if to==0:
#         return
#     n[0] += 1
#     solve(n, to-1)

# n = int(input())
# x = [n]
# solve(x,15)
# print(x[0])

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # if not root1:
        #     return root2
        # if not root2:
        #     return root1

        def solve(root1, root2):
            if not root1:
                return root2
            if not root2:
                return root1
            res = TreeNode(root1.val+root2.val)
            res.left = solve(root1.left, root2.left)
            res.right = solve(root1.right, root2.right)
            return res

        return solve(root1, root2)
        