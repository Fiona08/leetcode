#104


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path  
# from the root node down to the farthest leaf node.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def maxDepthOfTree(self,root):
        if not root:
            return 0
        else:
            return max(self.maxDepthOfTree(root.left),self.maxDepthOfTree(root.right))+1
