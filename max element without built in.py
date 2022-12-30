def max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
list = [12,11,15,48,19]
print("largest number: ",max(list))
