class Circle:
    def area(self):
        self.r=int(input("Enter the radius of the circle"))
        res=3.14*self.r**2
        print("Area of the circle is ",res)
class Rectangle(Circle):
    def area(self):
        self.l=int(input("Enter the length of the rectangle :"))
        self.b=int(input("Enter the breadth of the rectangle :"))
        res=self.l*self.b
        print("Area of the rectangle is ",res)
        super().area()

class Square(Rectangle):
    def area(self):
        self.side=int(input("Enter the side of the suqare :"))
        res=self.side**2
        print("Area of the sqaure is: ",res)
        super().area()
s=Square()
s.area()
