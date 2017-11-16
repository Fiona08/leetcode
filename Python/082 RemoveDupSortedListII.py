#82


# Time:  O(n)
# Space: O(1)


# Given a sorted linked list, delete all nodes 
# that have duplicate numbers, 
# leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))
    
class ListSol():
    def removeDupSortedListII(self,head):
        if not head or not head.next:
            return head
        dummy=ListNode(-1)
        dummy.next=head
        prev,cur=dummy,head
        while cur:
            if cur.next and cur.next.val==cur.val:
                cur_val=cur.val
                while cur and cur.val==cur_val:
                    cur=cur.next
                prev.next=cur
            else:
                prev,cur=prev.next,cur.next
        return dummy.next
