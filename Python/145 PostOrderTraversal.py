#145  


# Time:  O(n)
# Space: O(1)
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def postOrderTraversal(self,root):
        if not root:
            return []
        stack,post_order,isvisited=[root],[],[]
        while stack:
            cur=stack.pop()
            if cur in isvisited:
                post_order.append(cur.val)
            else:
                if cur.right is not None:
                    stack.append(cur)
                    isvisited.append(cur)
                    stack.append(cur.right)
                else:
                    stack.append(cur)
                    isvisited.append(cur)
                if cur.left is not None:
                    stack.append(cur.left)
        return post_order
