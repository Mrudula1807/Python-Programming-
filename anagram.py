s1=input("enter the 1st string: ")
s2=input("enter the 2st string: ")
def check(s1,s2):
    if(sorted (s1)==sorted(s2)):
        print("the string is anagram")
    else:
        print("the string is not anagram")
check(s1,s2)
