arr = []
num = int(input("How many numbers: "))
for n in range(num):
    numbers = int(input("Enter numbers:"))
    arr.append(numbers)
print("Maximum element : ", max(arr), "\nMinimum element : ", min(arr))

