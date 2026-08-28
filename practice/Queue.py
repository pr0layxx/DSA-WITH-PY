class Queue:
    def __init__(self):
        self.items= []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self, value):
        return self.items.append(value)
    
    def delete(self):
        if self.isEmpty() :
            print("Queue is empty")
        else:
            return self.items.pop(0)

q = Queue()
print(q.isEmpty())
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())
q.insert(40)
print(q.delete())