# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,maxSoFar):
            if not node:
                return 0 
            
            isGoodNode = node.val>= maxSoFar 
            maxSoFar = max(node.val,maxSoFar)
            return isGoodNode + dfs(node.left,maxSoFar) + dfs(node.right,maxSoFar)            

        return dfs(root,root.val)

        