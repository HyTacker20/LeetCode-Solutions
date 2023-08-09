# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def __str__(self):
        return f"ListNode(val: {self.val}, next: {self.next})"


l1 = ListNode(val=0, next=ListNode(val=0, next=ListNode(val=1)))
l2 = ListNode(val=9, next=ListNode(val=9))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val_sum = l1.val + l2.val
        if not l1.next and l2.next:
            l1, l2 = l2, l1
        if not l2.next and l1.next:
            l2.next = ListNode()
            if l1.val + l2.val >= 10:
                l2.next.val += 1
            return ListNode(val=val_sum % 10, next=self.addTwoNumbers(l1=l1.next, l2=l2.next))
        elif not l1.next and not l2.next:
            return ListNode(val_sum % 10, next=ListNode(val_sum // 10) if val_sum >= 10 else None)
        else:
            if l1.val + l2.val >= 10:
                l1.next.val += 1
            return ListNode(val=(l1.val + l2.val) % 10, next=self.addTwoNumbers(l1.next, l2.next))


sol = Solution()
print(sol.addTwoNumbers(l1, l2))
