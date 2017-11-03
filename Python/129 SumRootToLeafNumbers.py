#129


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123. 
# Find the total sum of all root-to-leaf numbers.
# 
# For example, 
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Return the sum = 12 + 13 = 25.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def sumRootToLeafNumbers(self,root,num=0):
        if not root:
            return 0
        if not root.left and not root.right:
            return num*10+root.val
        
        return self.sumRoottoLeafNumbers(root.left,num*10+root.val)+self.sumRoottoLeafNumbers(root.right,num*10+root.val)
