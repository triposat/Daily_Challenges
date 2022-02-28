# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = root
        if not root:
            return TreeNode(val)
        new = TreeNode(val)
        while root:
            if root.val<val:
                if root.right is None:
                    root.right = new
                    break
                root=root.right
            else:
                if root.left is None:
                    root.left = new
                    break
                root=root.left
        return ans