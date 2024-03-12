# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=dict()
        pre=0
        dummy=ListNode(0,head)
        d[0]=dummy
        while(head!=None):
            pre+=head.val
            if pre in d:
                dum=d[pre]
                k=dum
                p=pre
                while(k!=head):
                    k=k.next
                    p+=k.val
                    if k!=head:
                        del d[p]
                dum.next=k.next
            else:
                d[pre]=head
            head=head.next
        return dummy.next
            
    