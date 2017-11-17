#160


# Time:  O(n)
# Space: O(1)


# Write a program to find the node at which 
# the intersection of two singly linked lists begins.
#
# For example, the following two linked lists:
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))
    
class ListSol():
    def intersectionOfTwoList(self,head1,head2):
        cur1,cur2,tail1,tail2=head1,head2,None,None
        while cur1 and cur2:
            if cur1==cur2:
                return cur1
            
            if cur1.next:
                cur1=cur1.next
            elif tail1 is None:
                tail1=cur1
                cur1=head2
            else:
                break
            if cur2.next:
                cur2=cur2.next
            elif tail2 is None:
                tail2=cur2
                cur2=head1
            else:
                break       
        return None
