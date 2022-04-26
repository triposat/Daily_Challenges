# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        que = [root]
        res = []
        while que:
            temp = []
            for _ in range(len(que)):
                ele = que.pop(0)
                temp.append(ele.val)
                if ele.left:
                    que.append(ele.left)
                if ele.right:
                    que.append(ele.right)
            res.append(sum(temp))
        res = enumerate(res)
        return max(res, key=lambda x: x[1])[0]+1