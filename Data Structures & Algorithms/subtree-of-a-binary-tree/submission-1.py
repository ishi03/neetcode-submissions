# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            if x.val != y.val:
                return False
            return isSameTree(x.left, y.left) and isSameTree(x.right, y.right)

        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        lt = self.isSubtree(root.left, subRoot)
        rt = self.isSubtree(root.right, subRoot)

        return lt or rt
        