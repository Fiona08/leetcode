#100


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given two binary trees, write a function to check if they are equal or not.
#
# Two binary trees are considered equal if they are structurally identical  
# and the nodes have the same value.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None
        
class treeSol():
    def isSameTree(self,root1,root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2:
            return root1.val==root2.val and self.isSameTree(root1.left,root2.left) and self.isSameTree(root1.right,root2.right)
        
        return False  
