class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class singlyLL:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):
        temp = Node(value)
        t1 = self.head
        if self.head != None:
            while t1.next != None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBeg(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while t1.next != None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
            
    def deleteLL(self, value):
        t1= self.head
        prev= t1
        if t1.data == value:
            self.head = t1.next
        while t1.next != None:
            if t1.data== value:
                prev.next = t1.next
                break
            prev = t1
            t1 = t1.next
        if t1.next == None:
            prev.next =None
            
    def printLL(self):
        t1 = self.head
        while t1.next != None:
            print(t1.data)
            t1 = t1.next
        print(t1.data)
    
    

obj = singlyLL()
obj.insertAtEnd(20)
obj.insertAtBeg(10)
obj.insertAtMid(15, 10)
obj.deleteLL(47)

obj.printLL()
