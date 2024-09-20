#Head and Tail Nodes
#Each Node is linked
#There are also doubly linked lists
#Null terminated, signifying the end of the list

#Big O
#prepend O(1)
#append O(1)
#lookup O(n)
#insert O(n)
#delete O(n)

class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def appendToBeginning(self, value) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def appendToEnd(self, value) -> None:
        node = Node(value)

        #Edge to make sure Linked List is not empty
        if self.head is None:
            self.head = node
        
        #Traverse through the Linked List to find the end, and append node to the end
        current = self.head
        while(current.next is not None):
            current = current.next
        current.next = node
    
    def printLinkedList(self):
        current = self.head

        while(current is not None):
            print(current.value)
            current = current.next


l = LinkedList()
l.appendToBeginning(4)
l.appendToBeginning(5)
l.appendToEnd(6)
l.printLinkedList()

