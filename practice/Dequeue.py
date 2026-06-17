class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    def insertAtFront(self, value):
        return self.items.insert(0,value)
    
    def deleteAtFront(self):
        if self.isEmpty() :
            return print("Dequeue is empty")
        else:
            return self.items.pop(0)

    def insertAtRear(self, value):
        return self.items.append(value)

    def deleteAtRear(self):
        if self.isEmpty():
            print("Dequeue is empty")
        else:
            return self.items.pop()
    
    
q = Dequeue()
print(q.isEmpty())
q.insertAtFront(10)
q.insertAtRear(20)
print(q.deleteAtRear())