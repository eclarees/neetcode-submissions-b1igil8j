# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverseTree(root): 
            res = [] 

            def dfs(root):
                if not root:
                    res.append(None)
                    return
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)

            dfs(root)
            return res

        p_res = traverseTree(p)
        q_res = traverseTree(q)
        print(p_res,q_res)
        if p_res == q_res:
            return True
        return False

            

        