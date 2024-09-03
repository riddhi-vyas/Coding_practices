# https://blog.boot.dev/computer-science/binary-search-tree-in-python/

from graphviz import Digraph # to visualize tree graphically

class BSTNode:
    def __init__(self, data=None):
        # initialize node with data
        self.data = data

        #if node has a data, create left and right child nodes
        if self.data:
            self.left = BSTNode()
            self.right = BSTNode()
        #if node has no data, set left and right to None
        else: 
            self.left = None
            self.right = None

    def insert(self, data):
        # if tree is empty, insert data here
        if self.data == None:
            self.data = data
            #create left and right childrem for inserted node
            self.left = BSTNode()
            self.right = BSTNode()
            print("{} is inserted successfully".format(self.data))
        elif data < self.data:
            self.left.insert(data)
            return
        elif data > self.data:
            self.right.insert(data)
            return
        elif data == self.data:
            return

    def inorder(self, root): # Left-Root-Right
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root): # Root-Left-Right
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root): # Left-Right-Root
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # To draw tree with nodes and edges    
    def add_nodes(self, dot: Digraph):
        if self.left:
            dot.node(str(self.left.data))
            dot.edge(str(self.data), str(self.left.data), label="L")
            self.left.add_nodes(dot)
        if self.right:
            dot.node(str(self.right.data))
            dot.edge(str(self.data), str(self.right.data), label="R")
            self.right.add_nodes(dot)

    # To visualize/export tree
    def visualize(self, filename = "bst"):
        dot = Digraph()
        dot.node(str(self.data))
        self.add_nodes(dot)
        dot.render(filename, view=True)

    # To print tree in terminal
    def print_tree(self, level=0, prefix="Root: "):
        if self.data is not None:
            print(" " * (level * 4) + prefix + str(self.data))
            if self.left:
                self.left.print_tree(level + 1, prefix="L--- ")
            if self.right:
                self.right.print_tree(level + 1, prefix="R--- ")

        
def main():
    # insert root node
    root1 = BSTNode(50)

    # insert 10 in BST
    root1.insert(10)
    root1.insert(20)
    root1.insert(35)
    root1.insert(25)
    root1.insert(70)
    root1.insert(55)
    root1.insert(90)

    #inorder traversal
    print("Inorder Traversal as below:")
    root1.inorder(root1)
    print()

     #preorder traversal
    print("Preorder Traversal as below:")
    root1.preorder(root1)
    print()

    #postorder traversal
    print("Postorder Traversal as below:")
    root1.postorder(root1)
    print()

    # Print tree in terminal
    print("\nBST:\n")
    root1.print_tree()

    # # to export tree in png form
    # root1.visualize("binary_search_tree") 

if __name__ == "__main__":
    main()

        
