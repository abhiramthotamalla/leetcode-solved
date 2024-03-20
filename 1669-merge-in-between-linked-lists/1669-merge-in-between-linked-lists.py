# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first=ListNode(-1,list1)
        while(a):
            first=first.next
            a-=1
        second=ListNode(-1,list1)
        b+=2
        while(b):
            second=second.next
            b-=1
        # print(first.val,second.val)
        first.next=list2
        while(first and first.next):
            first=first.next
        first.next=second
        return list1