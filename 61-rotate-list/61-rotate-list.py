# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        k = k % cnt
        if k == 0:
            return head
        temp = head
        for _ in range(cnt-k-1):
            temp = temp.next
        new = new1 = temp.next
        temp.next = None
        while new1.next:
            new1 = new1.next
        new1.next = head
        return new