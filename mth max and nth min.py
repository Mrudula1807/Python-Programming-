a=int(input("enter range: "))
A=[]
for i in range(a):
        b=eval(input("enter element: "))
        A.append(b)
c=sorted(A)
print(c)
m=int(input("M:"))
n=int(input("N:"))
s=c[-m]+c[n-1]
d=c[-m]-c[n-1]
print("Mth maximum:",c[-m])
print("Nth minimum:",c[n-1])
print("SUM:",s)
print("DIFFERENCE:",d)
