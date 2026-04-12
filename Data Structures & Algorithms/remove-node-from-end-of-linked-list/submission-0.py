# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmpVal = []
        first = head
        while first:
            tmpVal.append(first.val)
            first = first.next

        k = len(tmpVal) - n
        tmpVal.pop(k)

        if not tmpVal:
            return None

        new_head = ListNode(tmpVal[0]) 
        current = new_head
        
        for val in tmpVal[1:]:
            new_node = ListNode(val)
            current.next = new_node  
            current = new_node 
        
        return new_head
        