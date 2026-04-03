# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN
        newHead = head
        turn_head = True
        while head and prev:
            if turn_head:
                nextHead = head.next
                head.next = prev
                head = nextHead
                turn_head = False
            else:
                nextPrev = prev.next
                prev.next = head
                prev = nextPrev
                turn_head = True
        # head = newHead
        # return newHead