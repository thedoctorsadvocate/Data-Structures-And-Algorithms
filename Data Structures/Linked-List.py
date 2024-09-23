import os
#Head and Tail Nodes
#Each Node is linked
#There are also doubly linked lists
#Null terminated, signifying the end of the list

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
    
    def insertAt(self, value, index) -> None:
        if index == 0:
            self.appendToBeginning(value)
        
        c = 0
        current = self.head

        while(current is not None and c + 1 != index):
            c += 1
            current = current.next
            
        if current is not None:
            node = Node(value)
            node.next = current.next
            current.next = node
                
        else:
            print('Index given is out of bounds')

    def popAtBeginning(self) -> None:
        current = self.head
        self.head = current.next

    def popAtEnd(self) -> None:
        current = self.head
        while(current is not None and current.next.next is not None):
            current = current.next
        current.next = None

    def popAtIndex(self, index) -> None:
        if index == 0:
            self.popAtBeginning()
        
        c = 0
        current = self.head

        while(current is not None and c + 1 != index):
            c = c + 1
            current = current.next
        
        if current is not None:
            current.next = current.next.next
        else:
            print('Index given is out of bounds')
        
    def getSize(self) -> None:
        size = 0

        current = self.head

        while(current is not None):
            current = current.next
            size += 1
        
        print(f'Size of the Linked List: {size}')

    def printLinkedList(self) -> None:
        current = self.head

        while(current is not None):
            print(current.value)
            current = current.next


link = LinkedList()
print('This is a Linked List. We will add a value "4" to the beginning.')
input('Press Enter to Continue')
os.system('cls')

link.appendToBeginning(4)
link.printLinkedList()
print('\nWe have added "4" to the beginning of the Linked List. Now we will add another value "5" to the beginning.')
input('Press Enter to Continue')
os.system('cls')

link.appendToBeginning(5)
link.printLinkedList()
print('\nWe have added "5" to the beginning of the Linked List. Now we will add another value "2" at the end of the list.')
input('Press Enter to Continue')
os.system('cls')

link.appendToEnd(2)
link.printLinkedList()
print('\nWe have added "2" to the end of the Linked List. Now we will add another value "3" at a positional index of "2"')
input('Press Enter to Continue')
os.system('cls')

link.insertAt(3, 2)
link.printLinkedList()
print('\nWe have added "3" to the "2" index of the Linked List. Now we will add another value "1" and "0" at the end of the list')
input('Press Enter to Continue')
os.system('cls')

link.appendToEnd(1)
link.appendToEnd(0)
link.printLinkedList()

print('\nLets now get the size of the Linked List')
input('Press Enter to Continue')
os.system('cls')
print('Size: ')
link.getSize()

input('\nPress Enter to Continue')
os.system('cls')
print('\nWe can also "pop" or remove certain nodes from the list. Lets remove one at the beginning, end, and then one in the middle section of the node.')

print('\nLinked List After "pop" from the beginning: ')
link.popAtBeginning()
link.printLinkedList()

input('Press Enter to Continue')
os.system('cls')
print('\nLinked List After "pop" from the end: ')
link.popAtEnd()
link.printLinkedList()

input('Press Enter to Continue')
os.system('cls')
print('\nLinked List After "pop" from the middle: ')
link.popAtIndex(2)
link.printLinkedList()