# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.add = 0
        def convertBST(root):
            if root:
                convertBST(root.right)
                root.val += self.add
                self.add = root.val
                convertBST(root.left)
        convertBST(root)
        return root