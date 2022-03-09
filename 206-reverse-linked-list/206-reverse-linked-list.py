# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative Approach:
        cur=head
        prev=None
        while cur:
            forw=cur.next
            cur.next=prev
            prev=cur
            cur=forw
        return prev
        
        # Recursive Approach:
        # def solve(head, prev):
        #     if not head:
        #         return prev
        #     n=head.next
        #     head.next=prev
        #     return solve(n ,head)
        # prev=None
        # return solve(head, prev)