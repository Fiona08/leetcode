#203


# Time:  O(n)
# Space: O(1)


# Remove all elements from a linked list of integers that have value val.
# 
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))
    
class ListSol():
    def removeListElem(self,head,target):
        dummy=ListNode(-1)
        #dummy.next=head
        prev,cur=dummy,head
        while cur:
            if cur.val==target:
                prev.next,cur=cur.next,cur.next
            else:
                prev.next=cur
                prev,cur=prev.next,cur.next
        return dummy.next
