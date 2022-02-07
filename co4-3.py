class  rectangle :
    
    def __init__(self,length,breadth):
        self.__length=length;
        self.__breadth=breadth;
    def area(self):
         self.a=self.__breadth*self.__length;
    def __lt__(self,other):
        if(self.a<other.a):
            return "Area of the 1st rectangle is less than the second"
        else:
            return "Area of the 2nd rectangle  is less than the first"
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
s1.area()
s2.area()
print(s1<s2)

    
