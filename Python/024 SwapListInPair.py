#24


# Time:  O(n)
# Space: O(1)


# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space. 
# You may not modify the values in the list, only nodes itself can be changed.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def swapListInPair(self,head):
        dummy=ListNode(-1)
        prev=dummy
        while head and head.next:
            next_one,next_two,next_three=head,head.next,head.next.next
            prev.next,next_two.next,next_one.next=next_two,next_one,next_three
            prev,head=next_one,next_three
        return dummy.next
