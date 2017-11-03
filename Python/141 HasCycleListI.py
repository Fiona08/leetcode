#141


# Time:  O(n)
# Space: O(1)


# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def hasCycleListI(self,head):
        fast,slow=head,head
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
            if fast == slow:
                return True
        return False
