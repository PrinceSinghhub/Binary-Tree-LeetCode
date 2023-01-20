# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def bfs(self, root):
        ans = []
        if root == None:
            return ans
        queue = deque()
        queue.append(root)

        while len(queue) != 0:
            level = []
            for _ in range(len(queue)):
                Node = queue.popleft()
                level.append(Node.val)

                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)

            ans.append(level)

        return ans

    def levelOrderBottom(self, root):

        ans = self.bfs(root)
        return ans[::-1]
