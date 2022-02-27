# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=[(root, 0)]
        width=0
        while q:
            size=len(q)
            mini=q[0][1]
            # width = max(width, q[-1][0]-q[0][0]+1) 
            first, last = 0,0
            for i in range(size):
                node=q[0][0]
                curr=q[0][1]-mini
                q.pop(0)
                if i==0:
                    first=curr
                if i==size-1:
                    last=curr
                if node.left:
                    q.append((node.left, 2*curr+1))
                if node.right:
                    q.append((node.right, 2*curr+2))
            width=max(width, last-first+1)
        return width