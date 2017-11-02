#2
 

# Time: O(n)
# Space: O(n)


# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None
    
    def __repr__(self):
        return '{}->{}'.format(self.val,repr(self.next))

class listSol():
    def addTwoNum(self,l1,l2):
        dummy=ListNode(-1)
        dummy.next=l1
        carry=0
        while l1 and l2:
            l1.val+=l2.val+carry
            l1.val,carry=l1.val%10,l1.val//10
            l1,l2=l1.next,l2.next
            
        if l2:
            l1=l2
        
        if carry:
            while l1:
                l1.val+=carry
                l1.val,carry=l1.val%10,l1.val//10
                l1=l1.next
        return dummy.next
