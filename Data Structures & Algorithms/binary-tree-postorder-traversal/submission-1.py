# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # # Recursive Approach
        # result = []
        # def dfs(node):
        #     if not node:
        #         return None
        #     dfs(node.left)
        #     dfs(node.right)
        #     result.append(node.val)
        # dfs(root)
        # return result

    # ITERATIVE APPROACH   
        res= []
        stack = [root]
        visit = [False]
        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return res
            
