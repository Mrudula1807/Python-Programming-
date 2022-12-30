list1 = [17,6,24,68,57,89,96]
count=0
for num in list1:
    if num % 2 != 0:
     count=count+1
     print(num, end=" ")
print("\n Number of odd numbers:",count)

