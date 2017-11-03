#94


# Time:  O(n)
# Space: O(1)


# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def inOrderTraversal(self,root):
        if not root:
            return []
        stack,in_order,isvisited=[root],[],[]
        while stack:
            cur=stack.pop()
            if cur in isvisited:
                in_order.append(cur.val)
            else:
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur)
                    isvisited.append(cur)
                    stack.append(cur.left)
                else:
                    stack.append(cur)
                    isvisited.append(cur)
        return in_order
