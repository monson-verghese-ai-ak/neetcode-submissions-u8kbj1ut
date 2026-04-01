# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge_two(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        
        if head1.val < head2.val:
            newHead = temp = head1
            head1 = head1.next
        else:
            newHead = temp = head2
            head2 = head2.next

        while head1 and head2:
            if head1.val < head2.val:
                temp.next = head1            
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = head2            
                temp = temp.next
                head2 = head2.next
        
        while head1:
            temp.next = head1            
            temp = temp.next
            head1 = head1.next        
    
        while head2:
            temp.next = head2            
            temp = temp.next
            head2 = head2.next

        return newHead

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        head1 = lists[0]
        for head2Idx in range(1, len(lists)):
            head1 = self.merge_two(head1, lists[head2Idx])
        return head1