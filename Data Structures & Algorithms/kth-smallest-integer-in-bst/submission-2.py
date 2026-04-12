# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return 0

        q = deque()
        q.append(root)  
        values = []

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                values.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        values.sort()
        print(values)

        return values[k-1]



