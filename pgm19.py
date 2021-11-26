start=int(input("Enter the Start year:"))
end=int(input("Enter end year:"))
while(start<=end):
    if((start%4==0)or((start%400==0)and(start%100!=0))):
        print(start,end=' ')
        start+=1
    else:
        start+=1
