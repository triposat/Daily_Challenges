# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative
# class Solution:
#     def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
#         if not root:
#             return []
#         stack = [(root, None)]
#         while stack:
#             node, parent = stack.pop()
#             if not node:
#                 continue
#             if node.val < low:
#                 node.left = None
#                 if parent:
#                     parent.left = node.right
#                 else:
#                     root = node.right
#             elif node.val > high:
#                 node.right = None
#                 if parent:
#                     parent.right = node.left
#                 else:
#                     root = node.left
#             else:
#                 parent = node
#             stack += [(child, parent) for child in (node.left, node.right)]
#         return root

# Recursive
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None 
        if root.val<low:
            root = self.trimBST(root.right, low, high)
        elif root.val>high:
            root = self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root