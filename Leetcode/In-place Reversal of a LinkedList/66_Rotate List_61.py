# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        last=head
        n=1

        while last.next != None:
            n+=1
            last=last.next


        k=k%n
        if k==0:
            return head

        count=1
        t=head

        while t != None:
            if count==n-k:
                break
            count+=1
            t=t.next

        last.next=head
        res=t.next
        t.next=None

        return res