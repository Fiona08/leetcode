# 144 preOrderTraversal


# Time:  O(n)
# Space: O(1)


# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
def preOrderTraversal(self, root):
        if not root:
            return []
        stack,pre_order=[root],[]
        while stack:
            cur=stack.pop()
            pre_order.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)
        return pre_order
