from doublyLinkedBase import _DoublyLinkedBase
from utility import Empty

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element
    
    def insert_first(self,e):
        self._insert_between(e,self._header,self._header._next)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        
    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)

    

