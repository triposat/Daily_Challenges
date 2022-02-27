# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative Approach
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         stack += node.left, node.right
        # return root
        
        # Recursive Approach
        if node:
            node.left, node.right = self.invertTree(node.right), self.invertTree(node.left)
            return node