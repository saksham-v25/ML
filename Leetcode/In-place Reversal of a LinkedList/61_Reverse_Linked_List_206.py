# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from typing import Optional, List
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr!=None:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex

        return prev
        