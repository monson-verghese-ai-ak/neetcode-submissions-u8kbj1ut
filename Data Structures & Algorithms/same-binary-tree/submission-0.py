# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if (not root1 and root2) or (not root2 and root1):
            return False
        if root1.val != root2.val:
            return False
        return self.recurse(root1.left, root2.left) and self.recurse(root1.right, root2.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        return self.recurse(p, q)