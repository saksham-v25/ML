# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        t=head
        before=None
        pos=1

        if head==None:
            return None
        if left==right:
            return head
        
        while t!=None:
            if pos<left:
                before=t
                t=t.next
                pos+=1
                continue
            break
        time=right-left+1
        curr=t
        prev=None

        while time>0:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            time-=1
            
        t.next=curr

        if before is None:
            head=prev
        else:
            before.next = prev
       
        return head