# Traversals time complexity = O(n), space comp = O(n)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Inorder(root):
        if root:
            Inorder(root.left)
            print(root.data, end=" ")
            Inorder(root.right)

def Preorder(root):
     if root:
          print(root.data, end=" ")
          Preorder(root.left)
          Preorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end=" ")

def BFS_Traversal(root):
    if root is None:
        return
    result = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        result.append(queue[0].data)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result

def height_of_tree(root):
    if not root:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    if left_height > right_height:
        return left_height+1
    else:
        return right_height+1 
        

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("--------Inorder Traversal---------")
    Inorder(root)
    print()
    print("--------Preorder Traversal---------")
    Preorder(root)
    print()
    print("--------Postorder Traversal---------")
    Postorder(root)
    print()
    print(f"Height of given tree: {height_of_tree(root)}")
    print("--------Breadth First Search(Level) Traversal---------")
    bfs_result = BFS_Traversal(root)
    print(bfs_result)

if __name__ == "__main__":
    main()


