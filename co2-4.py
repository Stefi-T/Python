import math

lists =[]
start=int(input("Enter start "))
end=int(input("Enter end "))
for a in range(start,end+1):
    for b in str(a):
        if int(b) % 2 != 0:
            break
    else:
        root=math.sqrt(a)
        if root % 1 == 0:
            lists.append(a)
print(lists)
        
