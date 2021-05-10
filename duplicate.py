new_lst=[2,4,5,6,3,2,4,5]
list=[]
for item in new_lst:
    if item not in list:
        list.append(item)
print(list)

