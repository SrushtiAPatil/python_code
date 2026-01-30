class Student:
    def stddata(self):
        self.num=int(input("Enter student number :"))
        self.name=input("Enter Student Name :")
        self.marks=float(input("Enter marks of Student :"))
class Employee:
    def empdata(self):
        self.num=int(input("\nEnter Employee number :"))
        self.name=input("Enter Student Name :")
class Teacher:
    def tracherddata(self):
        self.name=input("\nEnter Teacher Name :")
        self.exp=float(input("Enter teacher experience :"))
        self.subject=input("Enter subject of the teacher :")
class Alldisplay:
    @classmethod
    def classlevel(cls,obj,info):
        cls.display(obj,info)


    @staticmethod
    def display(obj,info):
        print("==="*20)
        print(type(obj))
        print("{} informatiom :".format(info))
        for k,v in obj.__dict__.items():
            print(k,"------->",v)

s=Student()
e=Employee()
t=Teacher()
s.stddata()
e.empdata()
t.tracherddata()
#calling with object name
a=Alldisplay()
a.classlevel(s,"Student")
a.classlevel(e,"Employee")
a.classlevel(t,"Teacher")