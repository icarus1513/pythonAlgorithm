# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = head
        if not start:
            return None
        while start.next:
            tmp = start.val
            start.val = start.next.val
            start.next.val = tmp
            start = start.next.next
            if not start:
                break
        return head