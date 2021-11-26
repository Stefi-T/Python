print("Enter the number")
n=int(input())
r=0
while(n>0):
    dig=n%10
    r=r+dig
    n=n//10
print("The sum of digits is:",r)
