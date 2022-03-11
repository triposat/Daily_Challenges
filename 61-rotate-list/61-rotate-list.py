# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head
        cnt=0
        while temp:
            cnt+=1
            temp=temp.next
        k=k%cnt
        if k==0:
            return head
        temp=head
        for i in range(cnt-k-1):
            temp=temp.next
        le=me=temp.next
        temp.next=None
        while me.next:
            me=me.next
        me.next=head
        return le