s=input("Enter value : ")
s=s.split(",")
l=[]
c=0
for i in s:
    l.append(int(i))
for i in l:
    if i>100:
        l[c]='over'
    c+=1
print(l)
