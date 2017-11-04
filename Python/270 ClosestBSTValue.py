#270


# Time:  O(h) height of BST
# Space: O(1)


# Given a non-empty binary search tree and a target value, 
# find the value in the BST that is closest to the target.


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class binarySearchTree():
    def closestBSTValue(self,root,target):
        difference=float('Inf')
        while root:
            if abs(root.val-target)<difference:
                difference=abs(root.val-target)
                closest_node=root
            elif root.val==target:
                return root
            elif root.val<target:
                root=root.right
            else:
                root=root.left
        return closest_node
