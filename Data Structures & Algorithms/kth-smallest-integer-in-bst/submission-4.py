# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def dfs(node):
            if not node:
                return 
            
            left = dfs(node.left)
            if left is not None:
                return left
            self.k -= 1
            if self.k == 0:
                return node.val
            return dfs(node.right)

        return dfs(root)


        # if not root:
        #     return 0

        # q = deque()
        # q.append(root)  
        # values = []

        # while q:
        #     for _ in range(len(q)):
        #         curr = q.popleft()
        #         values.append(curr.val)
        #         if curr.left:
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)

        # values.sort()

        # return values[k-1]



