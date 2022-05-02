# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q=[root]
        res=[]
        while q:
            temp=[]
            for _ in range(len(q)):
                ele = q.pop(0)
                temp.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            if len(res)&1:
                res.append(temp[::-1])
            else:
                res.append(temp)
        return res