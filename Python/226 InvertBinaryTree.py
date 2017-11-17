#226


# Time:  O(n)
# Space: O(h) h: the hegiht of the tree


# Invert a binary tree.
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def invertBinaryTree(self,root):
        if not root or (not root.left and not root.right):
            return root
        stack_node=[root.left,root.right]
        while stack_node:
            left,right=stack_node.pop(),stack_node.pop()
            if left is not None and right is not None:
                left.val,right.val=right.val,left.val
            
                stack_node.append(left.left)
                stack_node.append(right.right)
            
                stack_node.append(left.right)
                stack_node.append(right.left)

        return root
