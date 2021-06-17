# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ip = []
        for i in lists:
            while i:
                ip.append(i.val)
                i = i.next
        ip = sorted(ip)

        if not ip:
            return None
        for idx, val in enumerate(ip):
            if idx == 0:
                tmp = ListNode(val)
                tmp_head = tmp
                head = tmp_head
            else:
                tmp = ListNode(val)
                tmp_head.next = tmp
                tmp_head = tmp_head.next
        return head