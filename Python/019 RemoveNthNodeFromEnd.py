#19


# Time:  O(n)
# Space: O(1)


# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#   Given linked list: 1->2->3->4->5, and n = 2.
#   After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def removeNthNodeFromEnd(self,head,N):
        dummy=ListNode(-1)
        dummy.next=head
        fast,slow=dummy,dummy
        while N>0 and fast:
            fast,N=fast.next,N-1
        while fast.next:
            fast,slow=fast.next,slow.next
        slow.next = slow.next.next
        return dummy.next
