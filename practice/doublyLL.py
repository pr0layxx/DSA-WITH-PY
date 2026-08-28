class Node:
    def __init__(self, value=None):
        self.prev = None 
        self.data = value
        self.next = None
        
class doublyLL:
    def __init__(self, head=None):
        self.head = head
        
    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        t = self.head
        while t.next != None:
            t= t.next
        t.next = temp
        temp.prev = t
        
    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next= self.head
        self.head.prev = temp
        self.head = temp
    
    def insertAtMid(self,value, x):
        t = self.head
        
        while t.next != None:
            if t.data == x:
                break
            else :
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev= temp
        temp.prev = t
        t.next = temp
        
    def deletion(self, value):
        t = self.head
        if self.head == None:
            print("Linked List is empty")
            return
        if t.data == value:
            self.head = t.next
            self.head.prev= None
            return
        while t.next != None:
            if t.data == value:
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t= t.next
        if t.data == value:
            t.prev.next = None
        
                    


        
        
    def printLL(self):
        t1=self.head
        while t1 != None:
            print(t1.data)
            t1= t1.next
            
obj = doublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(29)
obj.insertAtBeg(1)
obj.insertAtBeg(2)
obj.insertAtMid(20,10)
obj.deletion(10)
obj.printLL()