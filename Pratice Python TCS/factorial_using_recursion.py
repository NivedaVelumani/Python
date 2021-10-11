""" In recursion function there will be 2case called base case and Recursive case
    base case is stoping condition
    recursive case is recursion that occurs 
    In this factorial base case is n=0 becoz it stops at 1 so that 0!=1
    recursive case is n(n-1)
"""
def fact(n):
     if n==0:
         return 1
     else:
         return n*fact(n-1)

n=int(input("Enter the number:"))
result=fact(n)
print(result)