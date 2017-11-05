#103

# Time:  O(n)
# Space: O(n)


# Given a binary tree, return the zigzag level order traversal of 
# its nodes' values. (ie, from left to right, then right to left 
# for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class BFSSol():
    def zigzagLevelOrderTraversalBT(self,root):
        level,next_level_node,zigzag_traversal=1,[root],[]
        while next_level_node:
            cur_level_node,cur_level_val=next_level_node,[]
            next_level_node=[]
            for cur_node in cur_level_node:
                cur_level_val.append(cur_node.val)
                if cur_node.left:
                    next_level_node.append(cur_node.left)
                if cur_node.right:
                    next_level_node.append(cur_node.right)
            if level%2:
                zigzag_traversal.append(cur_level_val)
            else:
                zigzag_traversal.append(cur_level_val[::-1])
            level+=1
        return zigzag_traversal
