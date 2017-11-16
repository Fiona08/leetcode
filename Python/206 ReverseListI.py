#206


# Time:  O(n)
# Space: O(1)


# Reverse a singly linked list.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))
    
class ListSol():
    def reverseListI(self,head):
        dummy=ListNode(-1)
        cur=head
        while cur:
            dummy.next,cur.next,cur=cur,dummy.next,cur.next
        return dummy.next 
