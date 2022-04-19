# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None
        def inOrder(root):
            if not root:
                return None
            inOrder(root.left)
            if self.prev:
                if root.val < self.prev.val:
                    if not self.first:
                        self.first = self.prev
                    self.second = root
            self.prev = root
            inOrder(root.right)
        inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val