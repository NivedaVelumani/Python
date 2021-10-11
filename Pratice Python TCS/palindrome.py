number=int(input("enter a string:"))
string=str(number)  #if it is a number we have to convert it to str
rev_string=string[::-1]
if string==rev_string:
    print("Palindrome")
else:
    print("Not a palindrome")