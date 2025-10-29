class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')
        return self._data.pop()

class EmptyError(Exception):
    def __init__(self,msg):
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return f"Empty Error: {self.msg}"
    

if __name__ == "__main__":
    testStack = ArrayStack()
    #testStack.push(1)
    print(testStack.top())