# Binary Tree Level Order Traversal
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeBFS:
    def __init__(self):
        self.prev = -sys.maxsize - 1

    def LevelOrder(self, root:TreeNode) -> list[list[int]]:
        if root is None:
            return []
        queue = [root]
        result = []

        while queue:
            current_level_size = len(queue) # no. of nodes at current level
            current_level_nodes = [] # list to store nodes at current level

            for _ in range(current_level_size):
                node = queue.pop(0)
                current_level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level_nodes)
        return result
    
# Validate BST - A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
    def IsValidBST(self, root:TreeNode) -> bool:
        # Approach: Using Inorder traversal -> if inorder traversal contains ascending order, it's BST otherwise not.
        return self.InOrder(root)
    
    def InOrder(self, root:TreeNode): #Left-Root-Right
        if root is None:
            return True
        if not self.InOrder(root.left):
            return False
        if root.val <= self.prev:
            return False
        self.prev = root.val
        return self.InOrder(root.right)
            

def main():
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    obj1 = BinaryTreeBFS()
    answer1 = obj1.LevelOrder(root1)
    print(f"Level Order Traversal of given tree: {answer1}")
    valid_bst1 = obj1.IsValidBST(root1)
    print(f"Given tree is Valid BST: {valid_bst1}")

if __name__ == "__main__":
    main()

    