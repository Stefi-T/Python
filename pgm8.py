print("Enter the string")
s=input()
print("Enter the index to be removed")
n=int(input())
s1=s[0:n]
s2=s[n+1:]
snew=s1+s2
print(snew)
