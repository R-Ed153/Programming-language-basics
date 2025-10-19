from abc import abstractmethod
from math import sqrt

class Polygon:
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass

class Triangle(Polygon):
    def  __init__(self,a:int,b:int,c:int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self)->int:
        return self.a+ self.b+ self.c
    def area(self)->float:
        semiPerimeter = self.perimeter() * 0.5
        area = sqrt(semiPerimeter * (semiPerimeter-self.a) * (semiPerimeter-self.b) * (semiPerimeter-self.c))
        return round(area,3)
    
class Quadrilateral(Polygon):
    def __init__(self,a:int,b:int,c:int,d:int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self)->int:
        return self.a + self.b + self.c + self.d
    
    def area(self)->float:
        pass

class EquilateralTriangle(Triangle):
    def __init__(self,side):
        super().__init__(side,side,side)
    

if __name__ == "__main__":
    testTriangle = Triangle(10,15,10)
    print("Area: ",testTriangle.area())
    print("Perimeter",testTriangle.perimeter()) 

    testEquilateralTriangle = EquilateralTriangle(10)
    print("Area: ",testEquilateralTriangle.area())
    print("Perimeter",testEquilateralTriangle.perimeter()) 


