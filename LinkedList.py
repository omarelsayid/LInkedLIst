class LinkedList:
    # Node of the linked list
    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    # Initialize the linked list
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the linked list
    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node after a given node
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be null")
            return
        new_node = self.Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Append a new node at the end of the linked list
    def append(self, new_data):
        new_node = self.Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Print the contents of the linked list starting from the given node
    def printList(self):
        tnode = self.head
        while tnode:
            print(tnode.data, end=" ")
            tnode = tnode.next

    # Delete a node with a given key
    def deleteNode(self, key):
        temp = self.head
        # If head node itself holds the key to be deleted
        if temp is not None and temp.data == key:
            self.head = temp.next
            temp = None
            return
        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next
        # If key was not present in linked list
        if temp is None:
            return
        prev.next = temp.next
        temp = None
