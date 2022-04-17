# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.pre = self.temp = TreeNode(0)
        def inOrder(root):
            if not root:
                return None
            inOrder(root.left)
            root.left = None
            self.pre.right = root
            self.pre = root
            inOrder(root.right)
        inOrder(root)
        return self.temp.right