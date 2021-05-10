
//list are muttable
numbers=[4,5,7,7,7,8,9]

numbers2=numbers.copy()
numbers.append(10)

print(numbers2)







number=[2,5,67,88,98]
max=number[0]
for num in number:
    if num > max:
        max=num
print(max)
