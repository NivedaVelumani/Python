# fibo = 0 1 1 2 3 5 8 13 21....

def fibo(n):
    a=0
    b=1


    for i in range (n):
        print(a)
        temp=a
        a=b
        b=temp + b

fibo(10)
