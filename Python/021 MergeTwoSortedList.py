#21


# Time:  O(n)
# Space: O(1)


# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def mergeTwoSortedList(self,l1,l2):
        dummy=ListNode(-1)
        cur=dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next,l1=l1,l1.next
            else:
                cur.next,l2=l2,l2.next
            cur=cur.next
        cur.next = l1 or l2
        return dummy.next
