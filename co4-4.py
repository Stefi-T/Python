class  time :
        def __init__(self,hour,minute,second):
                 self.__hour=hour;
                 self.__minute=minute;
                 self.__second=second;
        def __add__(self,other):
	          x=(self.__hour+self.__hour+(self.__minute+other.__minute+(self.__second+other.__second)//60)//60)%24
	          y=(self.__minute+other.__minute+(self.__second+other.__second)//60)%60
	          z=(self.__second+other.__second)%60
	          print(x,y,z)
print("Enter first Time")
print("hrs");
h1=int(input())
print("mins");
m1=int(input())
print("sec");
s1=int(input())
print("Enter second Time")
print("hrs");
h2=int(input())
print("mins");
m2=int(input())
print("sec");
s2=int(input())
obj1=time(h1,m1,s1)
obj2=time(h2,m2,s2)
print("Sum:")
obj1+obj2


