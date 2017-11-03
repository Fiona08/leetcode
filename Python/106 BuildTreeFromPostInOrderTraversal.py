#106


# Time:  O(n)
# Space: O(n)


# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def buildTreeFromPostInOrderTraversal(self,postOrder,inOrder):
        inOrder_val_indice={}
        for indice,val in enumerate(inOrder):
            inOrder_val_indice[val]=indice
        return self.buildTreeFromPostInOrderTraversalRec(postOrder,inOrder_val_indice,len(postOrder)-1,0,len(inOrder))
    def buildTreeFromPostInOrderTraversalRec(self,postOrder,inOrder_val_indice,post_end,in_start,in_end):
        if in_start==in_end:
            return None
        node=TreeNode(postOrder[post_end])
        node_indice_inOrder=inOrder_val_indice[postOrder[post_end]]
        node.left=self.buildTreeFromPostInOrderTraversalRec(postOrder,inOrder_val_indice,post_end-in_end+node_indice_inOrder,in_start,node_indice_inOrder)
        node.right=self.buildTreeFromPostInOrderTraversalRec(postOrder,inOrder_val_indice,post_end-1,node_indice_inOrder+1,in_end)
        return node
