"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hMap = {}
        x = y = head
        while x:
            hMap[x] = Node(x.val)
            x = x.next
        while y:
            hMap[y].next = hMap.get(y.next)
            hMap[y].random = hMap.get(y.random)
            y = y.next
        return hMap.get(head)