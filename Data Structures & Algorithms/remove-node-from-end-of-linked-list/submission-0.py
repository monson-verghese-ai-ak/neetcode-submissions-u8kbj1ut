# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        slow = None
        fast = head
        temp = head
        num_nodes = 1
        while temp:
            temp = temp.next
            num_nodes += 1
        
        idx = num_nodes - n - 1
        while idx:
            slow = fast
            fast = fast.next
            idx -= 1
        
        slow.next = fast.next
        return head