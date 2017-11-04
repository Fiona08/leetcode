#230



# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often 
# and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class binarySearchTree():
    def kthSmallestBST(self,root,k):
        visited_node,cur,rank=[],root,0
        while cur or visited_node:
            if cur:
                visited_node.append(cur)
                cur=cur.left
            else:
                cur=visited_node.pop()
                rank+=1
                if rank==k:
                    return cur.val                
                cur=cur.right
        return None
