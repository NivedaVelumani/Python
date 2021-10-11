"""
By using Euclid Theorem
a=64 b=48
64=48*X+remainder
64=48*1+16
48=16*3+0
16=0
import math
result=math.gcd(4,18)
print(result)

"""

def compute_gcd(a,b):
    if b==0:
        return a
    else:
        return compute_gcd(b,a%b)

num1=int(input("1st number:"))
num2=int(input("2nd number:"))
print(compute_gcd(num1,num2))