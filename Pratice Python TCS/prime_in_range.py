#This program will print the prime number ij the given range
start=int(input("Enter the starting range:"))
end=int(input("Enter the end range:"))
for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)

        