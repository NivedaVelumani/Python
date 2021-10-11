string=input("Enter a string:")
string=string.lower()
count=0
list=['a','e','i','o','u']
for char in string:
    if char in list:
        count=count+1
print(count)