n=int(input("which sequence of Fibonacci do you want to search"))
first=0
second=1
last=0
print(first,second,end=" ")
for i in range(2,n):
    last=first+second
    first=second
    second=last
    print(last,end=" ")
