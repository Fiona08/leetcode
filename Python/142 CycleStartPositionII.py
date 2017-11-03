#142


# Time:  O(n)
# Space: O(1)


# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.
#
# Note: Do not modify the linked list.
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
    def cycleStartPositionII(self,head):
        fast,slow=head,head
        while fast and fast.next:
            fast,slow=fast.next.next,slow.next
            if fast == slow:
                fast=head
                while fast is not slow:
                    fast,slow=fast.next,slow.next
                return fast
        return None
