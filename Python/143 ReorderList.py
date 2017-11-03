#143 



# Time:  O(n)
# Space: O(1)


# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def reorderList(self,head):
        slow,fast=head,head
        while fast and fast.next:
            prev,fast,slow=slow,fast.next.next,slow.next
        prev.next=None
        while slow:
            prev.next,slow.next,slow=slow,prev.next,slow.next
        head2,prev.next=prev.next,None
          
        dummy=ListNode(-1)
        cur=dummy
        while head and head2:
            cur.next,head=head,head.next
            cur=cur.next
            cur.next,head2=head2,head2.next
            cur=cur.next
            
        cur.next=head or head2
        return dummy.next
