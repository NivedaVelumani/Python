import sys

sys.setrecursionlimit(30)
print(sys.getrecursionlimit())

i=0

def greet():
    global i
    i+=1
    print("Recursion" ,i)
    greet()

greet()
