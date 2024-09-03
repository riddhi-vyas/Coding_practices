# Geeksforgeeks - https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1
# Given a Binary Tree, return Left/Right view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side and right view is when tree is seen from right side. 
# Left view solution approach: Preorder -> Root - Left - Right
# Right view solution approach: Reverse Preorder-> Root - Right - Left

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view(root):
    result = []
    left_recursion(root, result, level=0)
    return result

def left_recursion(root, result, level):
    if root == None:
        return
    if level == len(result):
        result.append(root.data)
    left_recursion(root.left, result, level+1)
    left_recursion(root.right, result, level+1)

def right_view(root):
    result = []
    right_recursion(root, result, level=0)
    return result

def right_recursion(root, result, level):
    if root == None:
        return
    if level == len(result):
        result.append(root.data)
    right_recursion(root.right, result, level+1)
    right_recursion(root.left, result, level+1)


def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.right = Node(3)

    left_tree = left_view(root)
    print(f"Left view of Binary Tree: {left_tree}")
    right_tree = right_view(root)
    print(f"Right view of Binary Tree: {right_tree}")

if __name__ == "__main__":
    main()