# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        flag = False
        que = [root]
        while que:
            curr = que.pop(0)
            if curr == None:
                flag = True
            else:
                if flag:
                    return False
                que.append(curr.left)
                que.append(curr.right)
        return True