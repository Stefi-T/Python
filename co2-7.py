st=input("Enter a string")
if(st[-3:]=='ing'):
    st=st[:]+'ly'
else:
    st=st[:]+'ing'
print(st)
