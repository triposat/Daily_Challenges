# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        temp=head
        hey=ListNode(0)
        me=hey
        res=defaultdict(int)
        while temp:
            res[temp.val] = res.get(temp.val, 0)+1
            temp=temp.next
        for ele in res:
            if res[ele]==1:
                hey.next=ListNode(ele)
                hey=hey.next
        return me.next