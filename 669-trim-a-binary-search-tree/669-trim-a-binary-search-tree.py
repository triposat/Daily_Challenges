# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return []
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if not node:
                continue
            if node.val < low:
                node.left = None
                if parent:
                    parent.left = node.right
                else:
                    root = node.right
            elif node.val > high:
                node.right = None
                if parent:
                    parent.right = node.left
                else:
                    root = node.left
            else:
                parent = node
            stack += [(child, parent) for child in (node.left, node.right)]
        return root