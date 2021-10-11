# import math
# re=math.lcm(24,48)
# print(re)


def compute_lcm(n1,n2):
    if n1>n2:
        higher=n1
    else:
        higher=n2
    value=higher
    while  True:
        if higher%n1==0 and higher%n2==0:
            print(higher)
            break
        else:
            higher=higher+value


n1=int(input("1st:"))
n2=int(input("2nd:"))
compute_lcm(n1,n2)
