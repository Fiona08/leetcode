#86


# Time:  O(n)
# Space: O(1)


# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
# 
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def partitionList1(self,head,target):
        dummy=ListNode(-1)
        dummy.next=head
        prev_first_larger=dummy
        
        while prev_first_larger.next.val<target:
            prev_first_larger=prev_first_larger.next
        prev,cur=prev_first_larger.next,prev_first_larger.next.next
        print(cur.val)
        while cur:
            if cur.val<target:
                prev_first_larger.next,cur.next,prev.next=cur,prev_first_larger.next,cur.next
                cur=prev.next
            else:
                prev,cur=cur,cur.next
        return dummy.next           
    def partitionList2(self,head,target):
        dummysmaller,dummygreater=ListNode(-1),ListNode(-1)
        smaller,greater=dummysmaller,dummygreater
        while head:
            if head.val<target:
                smaller.next,head=head,head.next
                smaller=smaller.next
            else:
                greater.next,head=head,head.next
                greater=greater.next
        smaller.next=dummygreater.next
        greater.next=None
        return dummysmaller.next
