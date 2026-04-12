# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True 
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(right-left)>1:
            return False

        # recursively check left and right height for all nodes
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self,root)->int:
            # height of tree is max height of left/right subtree 
            if not root:
                return 0 
            return max(self.height(root.left)+1,self.height(root.right)+1)


        
        