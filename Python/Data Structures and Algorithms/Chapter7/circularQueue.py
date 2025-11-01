from utility import Empty

class CircularQueue:
    class _Node:
        __slots__ = "_element", "_next"
        def __init__(self, element, next):
                self._element = element
                self._next = next
    
    def __init__(self):
        self._tail = None
        self._size = 0

        
