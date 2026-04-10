# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root, levels, level):
        if not root:
            return
        if level not in levels:
            levels[level] = [root.val]
        else:
            levels[level].append(root.val)
        self.recurse(root.left, levels, level+1)
        self.recurse(root.right, levels, level+1)
        return levels
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        levels = self.recurse(root, {}, 0)
        # print(type(levels.values()))
        return list(levels.values())