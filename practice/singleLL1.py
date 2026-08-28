class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next
        
class singlyLL:
    def __init__(self, head= None):
        self.head = head
        
        self.head = head
    
    def insertAtEnd(self, value):
        temp = Node(value)
        t1= self.head
        if self.head != None:
            while t1.next != None:
                t1= t1.next
            t1.next = temp
        else:
            self.head = temp
            
    def printLL(self):
        t1= self.head
        while t1.next!= None:
            print(t1.data)
            t1= t1.next
        print(t1.data)
        
obj = singlyLL()
obj.insertAtEnd(69)
obj.insertAtEnd(60)
obj.printLL()