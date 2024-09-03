# Morris Traversal for optimized space complexity - https://youtu.be/80Zug6D1_r4?si=DGkaQHbiayF7O_PT
# This is optimized approach as space complexity is optimized using threading tree concept
# Traversals: Preorder, Inorder 
# time complexity = O(n), space comp = O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Inorder(root): # Left - Root - Right
    in_list = []
    cur = root

    # Loop until the current node is not None
    while cur != None:
        # If the current node's left child is None
        if cur.left == None:
            # Add the value of the current node to the in_list
            in_list.append(cur.data)
            # Move to the right child
            cur = cur.right
        # If the left child is not None,
        # find the predecessor (rightmost node in the left subtree)
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
                
            # If the predecessor's right child is None, 
            # Establish a temporary link and move to the left child
            if prev.right == None:
                prev.right = cur
                cur = cur.left
            
            # If the predecessor's right child is already linked, remove the link,
            # add the current node to inorder list,
            # and move to the right child
            else:
                prev.right = None
                in_list.append(cur.data)
                cur = cur.right

    return in_list

def Preorder(root): # Root - Left - Right
    pre_list = []
    cur = root

    # Loop until the current node is not None
    while cur != None:
        # If the current node's left child is None
        if cur.left == None:
            # Add the value of the current node to the in_list
            pre_list.append(cur.data)
            # Move to the right child
            cur = cur.right
        # If the left child is not None,
        # find the predecessor (rightmost node in the left subtree)
        else:
            prev = cur.left
            while prev.right and prev.right != cur:
                prev = prev.right
                
            # If the predecessor's right child is None, 
            # add the current node to inorder list,
            # Establish a temporary link and move to the left child
            if prev.right == None:
                prev.right = cur
                pre_list.append(cur.data)
                cur = cur.left
            
            # If the predecessor's right child is already linked, remove the link,
            
            # and move to the right child
            else:
                prev.right = None
                cur = cur.right

    return pre_list

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.right = Node(3)

    print("--------Inorder Traversal---------")
    inorder_result = Inorder(root)
    print(inorder_result)
    print("--------Preorder Traversal---------")
    preorder_result = Preorder(root)
    print(preorder_result)

if __name__ == "__main__":
    main()


