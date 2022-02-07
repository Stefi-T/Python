
class  rectangle :
     def __init__(self,length,breadth):
        self.length=length;
        self.breadth=breadth;
       
     def area(self):
         return self.breadth*self.length;
     def p(self):
         return 2*(self.breadth+self.length);
print("enter length of 1st rectangle");
i=int(input())
print("enter breadth of 1st rectangle");
b=int(input())
print("enter length of 2st rectangle");
l=int(input())
print("enter breadth of 2st rectangle");
m=int(input())

s1=rectangle(i,b)
s2=rectangle(l,m)
e=s1.area()
x=s2.area()
if e>x:
    print("Area of rectangle 1 is great")

elif x>e:
      
      print("Area Of rectangle 2 is great")
else :
     print("both area are same",x)

