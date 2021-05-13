# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1 = ListNode()
        first = t1
        up = 0
        while True:
            tmp = ListNode()
            if l1 == None or l2 == None:
                if l1 == None and l2 == None:
                    break
                elif l1 == None:
                    l1 = ListNode()
                elif l2 == None:
                    l2 = ListNode()
            tmp.val = l1.val + l2.val
            if up != 0:
                tmp.val += up
                up = 0
            if tmp.val >= 10:
                up = int(tmp.val / 10)
                tmp.val = tmp.val % 10
            while t1.next:
                t1 = t1.next
            l1 = l1.next
            l2 = l2.next
            t1.next = tmp
        if up != 0:
            last = ListNode()
            last.val = up
            t1.next.next = last
        first = first.next
        return first
