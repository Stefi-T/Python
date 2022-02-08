print("Enter the number of terms")
n=int(input())
i = 0
first = 0
second = 1
temp = 0
while(i < n):
    if(i <= 1):
            Next = i
    else:
        Next = first + second
        first = second
        second = Next
    print(Next)
    i = i + 1
