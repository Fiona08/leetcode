#285


# Time:  O(h) height of BST
# Space: O(1)


# Given a binary search tree and a node in it, 
# find the in-order successor of that node in the BST.
#
# Note: If the given node has no in-order successor 
# in the tree, return null.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class binarySearchTree():
    def inOrderSuccessorInBST(self,root,node):
        if node.right:
            node=node.right
            while node.left:
                node=node.left
            return node
        successor=None
        while root and root!=node:
            print(root.val)
            print('node ',node.val)
            if root.val>node.val:
                successor=root
                root=root.left
            else:
                root=root.right
        return successor
