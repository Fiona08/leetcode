#100 


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def isBalancedTree(self,root):
        return self.heightOfTree(root)>=0
    def heightOfTree(self,root):
        if not root:
            return 0
        left_height,right_height=self.heightOfTree(root.left),self.heightOfTree(root.right)
        if left_height<0 or right_height<0 or abs(left_height-right_height)>1:
            return -1
        return max(left_height,right_height)+1
