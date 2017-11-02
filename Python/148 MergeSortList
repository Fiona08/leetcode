#148


# Time:  O(nlogn)
# Space: O(logn) for stack cal


# Sort a linked list in O(n log n) time using constant space complexity.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def mergeSortList(self,head):
        if not head or not head.next:
            return head
        
        fast,slow,prev=head,head,None
        while fast and fast.next:
            fast,slow,prev=fast.next.next,slow.next,slow
        prev.next=None
        
        sorted_l1=self.mergeSortList(head)
        sorted_l2=self.mergeSortList(slow)
        
        return self.mergeTwoList(sorted_l1,sorted_l2)
    def mergeTwoList(self,l1,l2):
        dummy=ListNode(-1)
        cur=dummy
        while l1 and l2:
            if l1.val<l2.val:
                cur.next,l1=l1,l1.next
                cur=cur.next
            else:
                cur.next,l2=l2,l2.next
                cur=cur.next
        cur.next=l1 or l2
        return dummy.next
