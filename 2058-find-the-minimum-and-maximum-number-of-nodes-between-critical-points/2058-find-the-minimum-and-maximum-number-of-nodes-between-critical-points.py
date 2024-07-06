# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i=1
        mini,maxi=float("inf"),-1*float("inf")
        prev=head.val
        head=head.next
        dum=[]
        while(head.next):
            if prev<head.val and head.val>head.next.val:
                dum.append(i)
            if prev>head.val and head.val<head.next.val:
                dum.append(i)
            i+=1
            prev=head.val
            head=head.next
        dum.sort()
        print(*dum)
        for i in range(1,len(dum)):
            mini=min(mini,dum[i]-dum[i-1])
        if len(dum)>1:
            maxi=max(maxi,dum[-1]-dum[0])
        if mini==float("inf"):
            mini=-1
        if maxi==-1*float("inf"):
            maxi=-1
        return [mini,maxi]