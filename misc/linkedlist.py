#linked list

class Node:

    # default value for node is None
    # unless arg given
    def __init__(self, val = None):
        self.value = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def addToHead(self, newNode):
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addToTail(self, newNode):
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode


if __name__ == "__main__":

    newNode = Node(5)
    #print(newNode.value)

    list1 = LinkedList()
    list1.addToHead(newNode)
    print(list1.head.value)

    newNode2 = Node(10)
    list1.addToTail(newNode2)
    print(list1.tail.value)

