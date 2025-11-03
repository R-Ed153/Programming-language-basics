from abc import ABC,abstractmethod

class Tree(ABC):
    class Position:
        @abstractmethod
        def element(self):
            pass

        @abstractmethod
        def __eq__(self,other):
            pass

        def __ne__(self,other):
            return not(self == other)
        
    @abstractmethod
    def root(self):
        pass

    @abstractmethod
    def parent(self,p):
        pass

    @abstractmethod
    def num_children(self,p):
        pass

    @abstractmethod
    def children(self,p):
        pass

    @abstractmethod
    def __len__(self):
        pass

    def is_root(self,p):
        return self.root() == p
    
    def is_leaf(self,p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self,p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
        
    def _height2(self,p):
        if self.is_leaf(p):
            return 0
        
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)