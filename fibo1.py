n = int(input("enter a number"))
a=0
b=1

for i in range(n):
    temp=a
    a=b
    b=temp+b
    print(a)
