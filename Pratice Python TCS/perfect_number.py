low=int(input("1st num:"))
high=int(input("2nd num:"))
for num in range(low,high+1):
    result=0
    for i in range(1,num):
        if num%i==0:
            result=result+i
    if result==num:
        print(num)
            