import operator
d={'january':31,'february':28,'March':31,'April':30,'may':31}
print("Ascending order of month names:")
sort=dict(sorted(d.items(),key=operator.itemgetter(0)))
print(sort)
print('enter a month')
m=input()
print(d[m])
print("Keys in alphabetical order:")
s=dict(sorted(d.items(),key=operator.itemgetter(1)))
print(s)
      
