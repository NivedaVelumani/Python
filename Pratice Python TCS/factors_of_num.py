num = int(input("Enter a number : "))
count=0
print("The factors are:")
for i in range(1,num+1):
    if(num % i == 0):
        count = count + 1
        print(i, end = " ")
print("\nTotal number of a factors:",count)
