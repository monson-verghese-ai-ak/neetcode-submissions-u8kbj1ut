# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root, p, q):
        # print(root.val, p.val, q.val)
        if root.val > p.val and root.val > q.val:
            return self.recurse(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.recurse(root.right, p, q)
        else:
            return root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        max_node = p if p.val > q.val else q
        min_node = p if p.val < q.val else q
        # print(max_node.val, min_node.val)
        return self.recurse(root, min_node, max_node)