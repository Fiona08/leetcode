#113


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree and a sum, find all root-to-leaf paths 
# where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None
    
class DFSSol():
    def pathSumBTII(self,root,target_sum):
        return self.pathSumBTIIRec(root,target_sum,[],[])
    def pathSumBTIIRec(self,root,target_sum,cur_path,result):
        if not root:
            return result
        if not root.left and not root.right and root.val==target_sum:
            result.append(cur_path+[root.val])
            return result
        cur_path.append(root.val)
        self.pathSumBTIIRec(root.left,target_sum-root.val,cur_path,result)
        self.pathSumBTIIRec(root.right,target_sum-root.val,cur_path,result)
        cur_path.pop()
        return result
