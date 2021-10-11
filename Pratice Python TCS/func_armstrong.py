number=int(input("Enter the number"))
def check_armstrong(num):
    sum=0
    original=num
    n=len(str(num))
    while num>0:
        dig=num%10
        sum=sum+dig**n
        num=num//10
    if sum== original:
        print("Armstrong Number")
    else:
        print("Not a Armstrong")

check_armstrong(number)