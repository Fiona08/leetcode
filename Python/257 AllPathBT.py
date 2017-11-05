#257


# Time:  O(n * h)
# Space: O(h)


# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]


class TreeNode():
    def __init__(self,val):
        self.val=val;
        self.right=None
        self.left=None

class BFSSol():
    def allPathBT(self,root):
        return self.allPathBTRec(root,[],[])
    def allPathBTRec(self,cur_node,cur_path,all_path):
        if not cur_node:
            return all_path
        if not cur_node.right and not cur_node.left:
            all_path.append('->'.join(str(x) for x in cur_path+[cur_node.val]))
            return all_path
        cur_path.append(cur_node.val)
        self.allPathBTRec(cur_node.left,cur_path,all_path)
        self.allPathBTRec(cur_node.right,cur_path,all_path)
        cur_path.pop()
        return all_path
