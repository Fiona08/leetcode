#112


# Time:  O(n)
# Space: O(h), h is height of binary tree



# Given a binary tree and a sum, determine if the tree
# has a root-to-leaf path such that adding up 
# all the values along the path equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf 
# path 5->4->11->2 which sum is 22.



class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None
    
class DFSSol():
    def pathSumBT(self,root,target_sum):
        if not root :
            return False
        if not root.left and not root.right and root.val==target_sum:
            return True
        #elif not root.left and not root.right and root.val!=target_sum:
        #    return False
        #elif root.left and not root.right:
        #    return self.pathSumBT(root.left,target_sum-root.val)
        #elif root.right and not root.left:
        #    return self.pathSumBT(root.right,target_sum-root.val)
        else :
            return self.pathSumBT(root.left,target_sum-root.val) or self.pathSumBT(root.right,target_sum-root.val)
