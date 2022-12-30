    #code to print the series in 1 plus 3 plus so on n

###
#n=int(input("Enter value: "))
#start,end = 1,n
#for n in range(start, end + 1):
 #   if n % 2 != 0:
 #       print(n, end = " + ")
###


n=int(input("Enter value: "))
odd=0
for n in range(1,n+1,2):
    #print("{0}".format(n))
    odd=odd+n
    #if n % 2 != 0:
print("the sum of odd numbers ={1}".format(n,odd))
