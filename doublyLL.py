class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None
        self.prev = None


class doublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        t = self.head
        while t.next != None:
            t = t.next
        t.next = temp
        temp.prev = t.next

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self, value, x):
        t = self.head
        while t.next != None:
            if t.data == x:
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t
        # print(temp)
        # print(temp.data)
        # print(temp.next)
        # print(temp.prev)

    def deleteNode(self, value):
        if self.head == None:
            print("Linked List is empty.")
            return
        t = self.head
        if t.data == value:
            self.head = t.next
            self.head.prev = None
            return
        while t.next != None:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            t = t.next
            if t.data == value:
                t.prev.next = None

    def printDoublyLL(self):
        t1 = self.head
        while t1.next != None:
            print(t1.data, end=" <--> ")
            t1 = t1.next
        print(t1.data)


obj = doublyLL()
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(10)
obj.insertAtMid(35, 30)
obj.deleteNode(35)
obj.printDoublyLL()
