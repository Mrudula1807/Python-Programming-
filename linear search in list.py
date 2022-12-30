def search(ele, key):
    for i in range(len(ele)):
        if ele[i] == key:
            return True
    return False
ele =[14,15,16,18,19,10]
key =16
if search(ele, key):
    print("element Found")
else:
    print("Not Found ")
