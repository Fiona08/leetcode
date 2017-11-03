#114


# Time:  O(n)
# Space: O(h), h is height of binary tree


# Given a binary tree, flatten it to a linked list in-place.
# 
# For example,
# Given
# 
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6
# The flattened tree should look like:
#    1
#     \
#      2
#       \
#        3
#         \
#          4
#           \
#            5
#             \
#              6


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class treeSol():
    flattenTree_to_list_=None
    def flattenTreeToList(self,root):
        if not root:
            return None
        self.flattenTreeToList(root.right)
        self.flattenTreeToList(root.left)
        root.right=self.flattenTree_to_list_
        root.left=None
        self.flattenTree_to_list_=root
        return root
