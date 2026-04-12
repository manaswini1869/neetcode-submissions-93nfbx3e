# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, val):
            if not node:
                return 0
            
            good = 1 if node.val >= val else 0
            val = max(node.val, val)

            return good + dfs(node.right, val) + dfs(node.left, val)

        return dfs(root, root.val)



        