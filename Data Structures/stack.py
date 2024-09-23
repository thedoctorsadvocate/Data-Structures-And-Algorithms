import os
#Stack is very similar to a linked list
#We need to track a head and next value to keep track of where we are
#main methods will be pop, push, peek
#also added methods to get the size as well as print the whole stack


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self) -> None:
        if self.isEmpty() is True:
            raise Exception("Stack is empty, cannot pop values from and empty stack")
        
        self.head = self.head.next
        self.size -= 1

    def peek(self) -> None:
        print(self.head.value)

    def getSize(self) -> int:
        return self.size
    
    def getStack(self) -> None:
        node = self.head
        output = ""
        while node is not None:
            output += str(node.value)
            if node.next is not None:
                output +=  " -> "
            node = node.next
        print(output)



myStack = Stack()

print('This is a Stack. We will add a value "10" to the Stack.\n(**Note that stacks are designed to "push" values to the beginning of the stack, so we will not be appending anything to the end or inserting in a particular index)')
input('Press Enter to Continue')
os.system('cls')
myStack.push(10)

print('Let us look at the Stack as a whole\n\n')
print('Stack Items:')
print('- - - - - - - - - - - - - - - - - - - - - - - - -\n')
myStack.getStack()
print('\n- - - - - - - - - - - - - - - - - - - - - - - - -')
size = myStack.getSize()
print(f'Size: {size}\n')

input('Press Enter to Continue')
os.system('cls')

print('Lets "push" a few more values to the stack. We will push "9", "8", and "7", and "6" and see how the stack is looking')
input('Press Enter to Continue')
os.system('cls')
myStack.push(9)
myStack.push(8)
myStack.push(7)
myStack.push(6)

print('Let us look at the Stack now\n\n')
print('Stack Items:')
print('- - - - - - - - - - - - - - - - - - - - - - - - -\n')
myStack.getStack()
print('\n- - - - - - - - - - - - - - - - - - - - - - - - -')
size = myStack.getSize()
print(f'Size: {size}\n')

print('Notice how the stack is counting backwards. This is by design. As a "push" method call will move the first value to the second place, and push the new value to the top.')
input('Press Enter to Continue')
os.system('cls')

print('Lets "pop" a couple of values. We will perform the "pop" operation twice. Lets see what happens')
input('Press Enter to Continue')
os.system('cls')
myStack.pop()

print('Popped Once\n\n')
print('Stack Items:')
print('- - - - - - - - - - - - - - - - - - - - - - - - -\n')
myStack.getStack()
print('\n- - - - - - - - - - - - - - - - - - - - - - - - -')
size = myStack.getSize()
print(f'Size: {size}\n')
input('Press Enter to Continue')
os.system('cls')

myStack.pop()

print('Popped Twice\n\n')
print('Stack Items:')
print('- - - - - - - - - - - - - - - - - - - - - - - - -\n')
myStack.getStack()
print('\n- - - - - - - - - - - - - - - - - - - - - - - - -')
size = myStack.getSize()
print(f'Size: {size}\n')
input('Press Enter to Continue')
os.system('cls')

print('Notice how the stack has removed the first two values from the beginning, in our case "6" was removed frist, then "7" was removed.')
print('Stacks operate in a LIFO order. Meaning the last item added to the stack will be the first to be removed.')
input('Press Enter to Continue')
os.system('cls')