def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter no. to find fact:"))
fact=fact(n)
print("Fact is",fact)
