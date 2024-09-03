# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if root:
            if root.left and root.right:
                return root.left.val < root.val and root.right.val > root.val    
        return self.inorder(root.left) and self.inorder(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # first create an array for storing inorder traversal of BST
        return self.inorder(root)
        
        