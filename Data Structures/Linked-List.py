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
        pass
    
    def printLinkedList(self):
        current = self.head

        while(current):
            print(current.value)
            current = current.next


l = LinkedList()
l.appendToBeginning(4)
l.appendToBeginning(5)
l.printLinkedList()

