def mul(n1, n2):
    return n1 * n2
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def div(n1, n2):
    return n1/ n2
value1 = int(input("Enter 1st number: "))
value2 = int(input("Enter 2nd number: "))
print("Select operation \n 1-Add \n 2-Sub \n 3-Multi \n 4-div \n")
choice = int(input("Choose 1/2/3/4: "))
if choice == 1:
    print(value1, "+", value2, "=", add(value1, value2))
elif choice == 2:
    print(value1, "-", value2, "=", sub(value1, value2))
elif choice == 3:
    print(value1, "*", value2, "=", mul(value1, value2))
elif choice == 4:
    print(value1, "/", value2, "=", div(value1, value2))
else:
   print("Enter correct operation:")
