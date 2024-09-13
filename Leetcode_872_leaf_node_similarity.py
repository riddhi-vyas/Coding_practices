# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeTraverse(self, root, result):
        if root:
            if root.left is None and root.right is None:
                result.append(root.val)
            if root.left:
                self.treeTraverse(root.left, result)
            if root.right:
                self.treeTraverse(root.right, result)

    def checkSimilarity(self, root, result):
        if root and len(result) > 0:
            if root.left is None and root.right is None:
                if result[0] == root.val: 
                    delete_element = result[0]
                    result.pop(0)
                    print(f"element to delete = {delete_element}")
                else:
                    return False
            if root.left:
                return self.checkSimilarity(root.left, result)
            if root.right:
                return self.checkSimilarity(root.right, result)
        
        if len(result) != 0:
            return False
        return True
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        res1 = []
        self.treeTraverse(root1, res1)
        # print(res1)
        return self.checkSimilarity(root2, res1)
    
    # def BFS_Traversal(self, root):
    #     if root is None:
    #         return
    #     result = []
    #     queue = []
    #     queue.append(root)
    #     while len(queue) > 0:
    #         result.append(queue[0].val)
    #         node = queue.pop(0)
    #         if node.left is not None:
    #             queue.append(node.left)
    #         if node.right is not None:
    #             queue.append(node.right)
    #     return result
            
def main():
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2, TreeNode(7), TreeNode(4))
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)
    root2.left = TreeNode(5, TreeNode(6), TreeNode(7))
    root2.right = TreeNode(1, TreeNode(4), TreeNode(2, TreeNode(9), TreeNode(8)))

    obj1 = Solution()
    answer = obj1.leafSimilar(root1, root2)
    print(f"Answer: {answer}")



    # obj1 = Solution()
    # obj2 = Solution()
    # tree_1 = obj1.BFS_Traversal(root1)
    # tree_2 = obj2.BFS_Traversal(root2)
    # print(f"root1 : {tree_1}")
    # print(f"root2 : {tree_2}")

if __name__ == "__main__":
    main()

        