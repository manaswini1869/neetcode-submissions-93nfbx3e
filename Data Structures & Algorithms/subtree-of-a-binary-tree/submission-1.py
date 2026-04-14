# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        if not root:
            return False

        def same(r, sr):
            if not r and not sr:
                return True
            if not r and sr:
                return False
            if not sr and r:
                return False
            if r.val == sr.val:
                return same(r.right, sr.right) and same(r.left, sr.left)
            
            return False
        
        if root.val == subRoot.val:
            return same(root, subRoot)
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




