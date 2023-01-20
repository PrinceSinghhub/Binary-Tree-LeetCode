# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            self.ans += abs(left - right)

            return root.val + left + right

        self.ans = 0
        dfs(root)
        return self.ans




