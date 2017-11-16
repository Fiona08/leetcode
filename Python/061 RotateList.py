#61


# Time:  O(n)
# Space: O(1)


# Given a list, rotate the list to the right by k places, 
# where k is non-negative.
#
# Example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


class ListSol():
    def rotateList(self,head,k):
        if not head:
            return None
        total_num_nodes=1
        cur=head
        while cur.next:
            cur=cur.next
            total_num_nodes+=1
        if not k%total_num_nodes:
            return head
        else:
            fast,slow=head,head
            for _ in range((k-1)%total_num_nodes):
                fast=fast.next 
            while fast.next:
                prev,slow,fast=slow,slow.next,fast.next
            prev.next=None
            fast.next=head
            return slow
