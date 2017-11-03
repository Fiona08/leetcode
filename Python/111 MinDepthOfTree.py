#111


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path 
# from the root node down to the nearest leaf node.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def minDepthOfTree(self,root):
        if not root:
            return 0

        if root.left and root.right:
            return min(self.minDepthOfTree(root.left),self.minDepthOfTree(root.right))+1
        else:
            return max(self.minDepthOfTree(root.left),self.minDepthOfTree(root.right))+1
