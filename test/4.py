# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  # type: ignore
        def add(
            l1: Optional[ListNode], l2: Optional[ListNode], carry: int
        ) -> Optional[ListNode]:
            if l1 is None and l2 is None and carry == 0:
                return None
            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0
            l1next = l1.next if l1 is not None else None
            l2next = l2.next if l2 is not None else None
            val = l1val + l2val + carry
            carry = val // 10
            val = val % 10
            return ListNode(val, add(l1next, l2next, carry))

        return add(l1, l2, 0)
