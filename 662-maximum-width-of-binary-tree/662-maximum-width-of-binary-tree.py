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
        que = [(root, 0)]
        width = 0
        while que:
            size = len(que)
            minInLevel = que[0][1]
            width = max(width, que[-1][1]-que[0][1]+1)
            for _ in range(size):
                node = que[0][0]
                curr = que[0][1]-minInLevel  # To prevent overflow...
                que.pop(0)
                if node.left:
                    que.append((node.left, 2*curr+1))
                if node.right:
                    que.append((node.right, 2*curr+2))
        return width