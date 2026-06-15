# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # BRUTE FORCE
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        # finding index of root in inorder
        idx = inorder.index(root_val)
        # left and right of inorder
        left_inorder = inorder[ : idx]
        right_inorder = inorder[idx+1 : ]
        # left and right subtree of preorder
        left_preorder = preorder[1 : 1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder) : ]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root