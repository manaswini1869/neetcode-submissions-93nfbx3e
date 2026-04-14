# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        temp = res = ListNode(-1)

        while l1 and l2:
            curr_sum = l1.val + l2.val
            new_node = ListNode(curr_sum % 10 + carry)
            carry = curr_sum // 10
            res.next = new_node
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            curr = l1.val + carry
            res.next = ListNode(curr % 10)
            carry = curr // 10
            res = res.next
        
        if l2:
            curr = l2.val + carry
            res.next = ListNode(curr % 10)
            carry = curr // 10
            res = res.next
        if carry:
            res.next = ListNode(carry)

        return temp.next






        