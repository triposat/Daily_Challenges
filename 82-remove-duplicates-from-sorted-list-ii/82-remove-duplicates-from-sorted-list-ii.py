# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        temp = head
        res = ListNode(0)
        res1 = res
        hasMap = defaultdict(int)
        while temp:
            hasMap[temp.val] = hasMap.get(temp.val, 0)+1
            temp = temp.next
        for ele in hasMap:
            if hasMap[ele] == 1:
                res.next = ListNode(ele)
                res = res.next
        return res1.next