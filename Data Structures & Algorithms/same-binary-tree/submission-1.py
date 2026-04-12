# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverseTreeDFS(root): 
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

        def traverseTreeBFS(root):
            from collections import deque

            res = []
            queue = deque([root])

            while queue:
                node = queue.popleft()
                if node is None:
                    res.append(None)
                    continue

                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            return res


        p_res = traverseTreeBFS(p)
        q_res = traverseTreeBFS(q)
        print(p_res,q_res)
        if p_res == q_res:
            return True
        return False

            

        