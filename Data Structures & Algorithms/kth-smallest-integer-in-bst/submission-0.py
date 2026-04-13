# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root, nodes):
        if not root:
            return
        self.inorder(root.left, nodes)
        nodes.append(root.val)
        self.inorder(root.right, nodes)
        return nodes
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = self.inorder(root, [])
        # print(nodes)
        return nodes[k-1]