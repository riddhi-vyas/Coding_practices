class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getList(self):
        p = self.head
        while p != None:
            print(p.data, end=" ")
            p = p.next
        print() # to add a line break

    def addAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAtPosition(self, data, pos):
        new_node = Node(data)
        # Case1- If position is 0
        if pos == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            return # exits function
        
        # Traverse to get previous element to pos
        prev = self.head
        curr = 0
        while prev is not None and curr < pos-1:
            prev = prev.next
            curr += 1

        # case2- If prev is None: position out of bounds
        if prev is None:
            print(f"Position {pos} is not available in list, Position out of bounds...")
            return # exits function
        # case3- If, pos is available in the list, Insert new_node after prev
        else:
            new_node.next = prev.next
            prev.next = new_node

        #case4-  If the new_node is inserted at end, update tail
        if new_node.next is None:
            self.tail = new_node

    def deleteFromPosition(self, pos):
        # if list is empty
        if self.head is None:
            print("List is empty")
            return
        #case1- if pos = 0
        if pos == 0:
            self.head = self.head.next
            if self.head is None: # if list had only one element which we deleted
                self.tail = None
            return
        # Traverse to find the prev node to the pos
        curr = 0
        prev = self.head
        while prev != None and curr < pos-1:
            prev = prev.next
            curr += 1

        #case2- If prev = None or prev.next = None: position out of bounds
        if prev == None or prev.next == None:
            print(f"posistion-{pos} not available in list, Position Out of Bounds..")
            return
        # case3- If node to be deleted is last node -> update tail
        if prev.next == None:
            self.tail = prev
        # case4- if prev.next is the node to be deleted
        if prev.next != None:
            prev.next = prev.next.next


def main():
    obj1 = LinkedList()
    obj1.addAtBegin(1)
    obj1.addAtEnd(5)
    obj1.addAtPosition(2,1)
    obj1.addAtPosition(3,2)
    obj1.addAtPosition(4,3)
    obj1.getList()
    pos = 2
    print(f"List after deleting element from position:{pos}")
    obj1.deleteFromPosition(pos)
    obj1.getList()
    obj1.deleteFromPosition(5)

if __name__ == "__main__":
    main()

