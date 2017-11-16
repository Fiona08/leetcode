#92


# Time:  O(n)
# Space: O(1)


# Reverse a linked list from position m to n.
# Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))
    
class ListSol():
    def reverseListII(self,head,start,end):
        dummy=ListNode(-1)
        dummy.next=head
        last_unreversed,first_reversed,reverse_num=None,dummy,end-start
        
        while start>0: 
            last_unreversed,first_reversed,start=first_reversed,first_reversed.next,start-1
        cur=first_reversed.next
        while reverse_num:
            cur.next,last_unreversed.next,cur,reverse_num=last_unreversed.next,cur,cur.next,reverse_num-1
        first_reversed.next=cur
        return dummy.next
