n=input("enter a string : ")
rev = n[::-1]
if n == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")
