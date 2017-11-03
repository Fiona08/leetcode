#105


# Time:  O(n)
# Space: O(n)


# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def buildTreeFromPreInOrderTraversal(self,preOrder,inOrder):
        inOrder_val_indice={}
        for indice,val in enumerate(inOrder):
            inOrder_val_indice[val]=indice
        return self.buildTreeFromPreInOrderTraversalRec(preOrder,inOrder_val_indice,0,0,len(inOrder))
    def buildTreeFromPreInOrderTraversalRec(self,preOrder,inOrder_val_indice,pre_start,in_start,in_end):
        if in_start==in_end:
            return None
        print(pre_start)
        node=TreeNode(preOrder[pre_start])
        
        node_indice_inOrder=inOrder_val_indice[preOrder[pre_start]]
        node.left=self.buildTreeFromPreInOrderTraversalRec(preOrder,inOrder_val_indice,pre_start+1,in_start,node_indice_inOrder)
        node.right=self.buildTreeFromPreInOrderTraversalRec(preOrder,inOrder_val_indice,pre_start+node_indice_inOrder-in_start+1,node_indice_inOrder+1,in_end)
        return node
