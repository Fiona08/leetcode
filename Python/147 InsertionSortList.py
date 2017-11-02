#147
    
 
 # Time: O(n^2)
 # Space: O(1)
 
 
# Sort a linked list using insertion sort


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def insertionSortList(self,head):
        if not head or self.isSorted(head):
            return head
        dummy=ListNode(-1)
        dummy.next=head
        last_sorted,cur=head,head.next
        while cur:
            prev=dummy
            while prev.next.val<cur.val:
                prev=prev.next
            if prev == last_sorted:
                last_sorted=cur
                cur=cur.next
            else:
                cur.next,prev.next,cur=prev.next,cur,cur.next
                last_sorted.next=cur
        return dummy.next
    
    def isSorted(self,head):
        while head and head.next:
            if head.val>head.next.val:
                return False
            else:
                head=head.next
        return True
