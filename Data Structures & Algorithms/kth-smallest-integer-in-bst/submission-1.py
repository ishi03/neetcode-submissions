# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left) # go as down in left branch as possible
            # process current node
            self.count += 1
            if self.count == k:
                self.res = root.val
            dfs(root.right)

        dfs(root)
        return self.res