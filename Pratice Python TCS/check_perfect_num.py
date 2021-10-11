"""perfect number is positive integer that is equal to the sum of this pos divisors exculding the number itself
eg: 6 -->1,2,3,6 exclude 6 
                sum=1+2+3=6

"""
num=int(input("Enter the num:"))
result=0
for i in range(1,num):
    if num%i==0:
        result=result+i
if result==num:
    print("Perfect number")
else:
    print("Not a Perfect")



