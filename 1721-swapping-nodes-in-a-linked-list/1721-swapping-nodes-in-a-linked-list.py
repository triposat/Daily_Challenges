# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start=end=head
        for i in range(1, k):
            start=start.next
        temp=start
        while temp and temp.next:
            end=end.next
            temp=temp.next
        start.val, end.val = end.val, start.val
        return head