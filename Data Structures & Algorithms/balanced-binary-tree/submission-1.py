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
        
        # check height of current tree root 
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left-right)>1:
            return False
        
        # if current tree is balanced, check for all subtrees below it
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def height(self,root):
        if not root:
            return 0 
        return max(self.height(root.left)+1,self.height(root.right)+1 )


        
        