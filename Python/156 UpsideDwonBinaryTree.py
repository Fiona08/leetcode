#156



# Given a binary tree where all the right nodes are either leaf nodes with a sibling 
# (a left node that shares the same parent node) or empty, flip it upside down 
# and turn it into a tree where the original right nodes turned into left leaf nodes. 
# Return the new root.
# 
# For example:
# Given a binary tree {1,2,3,4,5},
#     1
#    / \
#   2   3
#  / \
# 4   5
# return the root of the binary tree [4,5,2,#,#,3,1].
#    4
#   / \
#  5   2
#     / \
#    3   1  


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    # iterative
    def upsideDwonBinaryTree1(self,root):
        cur_node,parent,sibling=root,None,None
        while cur_node:
            cur_left=cur_node.left
            cur_node.left=sibling
            sibling=cur_node.right
            cur_node.right=parent
            parent=cur_node
            cur_node=cur_left
        return parent
    # recursive
    def upsideDwonBinaryTree2(self,root,parent=None):
        if not root:
            return parent
        inverse_tree=self.upsideDwonBinaryTree2(root.left,root)
        if parent:
            root.left=parent.right
        else:
            root.left=None
        root.right=parent
        return inverse_tree
