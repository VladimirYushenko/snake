class Node:

    def __init__(self, number):
        self.value = number
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add(self, nodeToAdd: Node):
        if self.head == None:
            self.head = nodeToAdd
        else:
            lastNode = self.head
            while lastNode.next != None:
                lastNode = lastNode.next
            lastNode.next = nodeToAdd
            

    def printAll(self):
        i = self.head
        while i != None:
            print(i.value)
            i = i.next



linkedList = LinkedList()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

linkedList.add(node1)
linkedList.add(node2)
linkedList.add(node3)
linkedList.add(node4)

linkedList.printAll()

