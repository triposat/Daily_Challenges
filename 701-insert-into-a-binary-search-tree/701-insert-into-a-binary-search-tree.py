class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        if not root:
            return TreeNode(val)
        node = TreeNode(val)
        while temp:
            if temp.val < val:
                if temp.right is None:
                    temp.right = node
                    break
                temp = temp.right
            else:
                if temp.left is None:
                    temp.left = node
                    break
                temp = temp.left
        return root
