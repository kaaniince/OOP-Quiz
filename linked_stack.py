class LinkedStack:
    class _Node:
        __slots__="_element","_next"
        def __init__(self,element,next):
            self._element = element
            self._next = next
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def push(self,e):
        self._head = self._Node(e,self._head)
        self._size +=1
    def top(self):
        if self.is_empty():
            return Exception("Stack is empty")
        return self._head._element
    def pop(self):
        if self.is_empty():
            return Exception("Stack is empty")
        top = self._head._element
        self._head = self._head._next
        self._size -=1
        return top
    
if __name__=="__main__":
        stack= LinkedStack()
        stack.push("A")
        stack.push("B")
        top = stack.pop()
        print(top)
        
class LinkedQueue:
        class _Node:
            __slots__="_element","_next"
            def __init__(self,element,next):
                self._element = element
                self._next = next
                
        def __init__(self):
            self._head=None
            self._size=0
            self._tail = None
        
        def __len__(self):
            return self._size
        
        def is_empty(self):
            return self._size == 0
        def first(self):
            if self.is_empty():
                raise Exception("Queue is empty")
            return self._head._element
        def dequeue(self):
            if self.is_empty():
                raise Exception("Queue is empty")
            top = self._head._element 
            self._head = self._head._next
            self._size -=1
            if self.is_empty():
                self._tail=None
            return  top
        def enqueue(self,e):
            newest = self._Node(e,None)
            if self.is_empty():
                self._head=newest
            else:
                self._tail._next= newest
            self._tail = newest
            self._size+=1   
if __name__=="__main__":
        queue= LinkedQueue()
        queue.enqueue("X")
        queue.enqueue("Y")
        queue.enqueue("Z")

        top = queue.dequeue()
        print(top)
    

        
        
    
    