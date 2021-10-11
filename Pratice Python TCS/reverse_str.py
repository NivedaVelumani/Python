def reverse(string):
    reverse_str=""
    for i in string:
        reverse_str=i+reverse_str
    print(reverse_str)
    # if ans==str:
    #     print("Palindrome")
    # else:
    #     print("Not a palindrome")

str=input("enter a string:")
print("Reversed String:")
reverse(str)

