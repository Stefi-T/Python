import math

t_area= lambda b,h : 1/2*(b*h)
r_area= lambda l,b : l*b
s_area= lambda a : a*a

s=int(input("Enter the breadth of triangle : "))
t=int(input("Enter the height of triangle : "))
print("Area of triangle : ",t_area(s,t))
u=int(input("Enter the length of rectangle : "))
v=int(input("Enter the breadth of rectangle : "))
print("Area of rectangle : ",r_area(u,v))
w=int(input("Enter the length of the sqaure : "))
print("Area of square : ",s_area(w))
