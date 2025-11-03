from tree import Tree
from abc import abstractmethod

class BinaryTree(Tree):
    @abstractmethod
    def left(self,p):
        pass

    @abstractmethod
    def right(self,p):
        pass

    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        
        else:
            if p == self.left(parent):
                return self.right(parent)
            
            else:
                return self.left(parent)
            
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
