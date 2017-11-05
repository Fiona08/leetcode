#102


# Time:  O(n)
# Space: O(n)


# Given a binary tree, return the level order traversal  
# of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
# return its level order traversal as:
# [
#  [3],
#  [9,20],
#  [15,7]
#]


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class BFSSol():
    def levelOrderTraversalBTI(self,root):
        if not root:
            return None
        next_level_node,levelOrder_Traversal=[root],[]
        while next_level_node:
            cur_level_node=next_level_node
            next_level_node,cur_level_val=[],[]
            
            for cur_node in cur_level_node:
                cur_level_val.append(cur_node.val)
                if cur_node.left:
                    next_level_node.append(cur_node.left)
                if cur_node.right:
                    next_level_node.append(cur_node.right)
            levelOrder_Traversal.append(cur_level_val)
        return levelOrder_Traversal
