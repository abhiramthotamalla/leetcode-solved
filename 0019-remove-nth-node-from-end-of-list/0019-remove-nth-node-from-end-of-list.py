# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=ListNode(0,head)
        left=dum
        k=n
        while(k and head):
            head=head.next
            k-=1
        while(head):
            head=head.next
            left=left.next
        left.next=left.next.next
        return dum.next