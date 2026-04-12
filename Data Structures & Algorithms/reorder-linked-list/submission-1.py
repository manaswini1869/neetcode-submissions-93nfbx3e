class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 🔧 FIX: split the list
        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        first, sec = head, prev
        while sec:
            t1, t2 = first.next, sec.next
            first.next = sec
            sec.next = t1
            first, sec = t1, t2
