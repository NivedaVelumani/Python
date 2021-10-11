n = int(input())
arr = []
for i in range(0,n):
    temp = int(input())
    arr.append(temp)
   # print(arr)
print("Reversed array is :")

for i in range(n-1,-1,-1):
    print(arr[i],end="")