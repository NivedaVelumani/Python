num=int(input("enter a num"))
result=0
#to find the len of the number we have convert it to str
n=len(str(num))
original=num
while(num!=0):
    digit=num%10
    result=result+digit**n
    num=num//10
if original==result:
    print("Armstrong")
else:
    print("Not")