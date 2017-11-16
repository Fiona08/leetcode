#83


# Time:  O(n)
# Space: O(1)


# Given a sorted linked list, delete all duplicates
# such that each element appear only once.
# 
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))
    
class ListSol():
    def removeDupSortedListI(self,head):
        #dummy=ListNode(-1)
        if not head or not head.next:
            return head
        prev,cur=head,head.next
        while cur:
            if cur.val!=prev.val:
                cur,prev=cur.next,prev.next
            else:
                prev.next,cur=cur.next,cur.next
        return head
