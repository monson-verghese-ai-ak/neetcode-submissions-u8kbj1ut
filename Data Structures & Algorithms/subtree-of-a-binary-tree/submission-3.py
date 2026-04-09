# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def recurse(self, root1, root2):
        if (not root1 and root2) or (not root2 and root1):
            return False
        if root1.val != root2.val:
            return self.recurse(root1.left, root2) or self.recurse(root1.right, root2)
        # print(root1.val, root2.val)
        return self.isSame(root1, root2) or self.recurse(root1.left, root2) or self.recurse(root1.right, root2)
    def isSame(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1):
            return False
        if root1.val != root2.val:
            return False
        # print(root1.val, root2.val)
        return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.recurse(root, subRoot)
        