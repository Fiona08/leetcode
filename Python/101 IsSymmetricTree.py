#101


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#     3    3
   
   
class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    def isSymmetricTree(self,root):
        if not root:
            return True
        stack=[root.left,root.right]
        while stack:
            cur1,cur2=stack.pop(),stack.pop()
            if cur1 is None and cur2 is None:
                pass
            elif cur1 is None or cur2 is None or cur1.val!=cur2.val:
                return False
            else:
                stack.append(cur1.left)
                stack.append(cur2.right)
                
                stack.append(cur1.right)
                stack.append(cur2.left)
        return True
