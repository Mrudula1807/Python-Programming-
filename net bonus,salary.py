n=int(input("Enter number of years : "))
s=int(input("Enter the salary: "))
if (n>5):
    bonus=(5/100*s)
    net_bonus=bonus*n*2
    net_salary=net_bonus+s
    print(net_bonus)
    print(net_salary)
else:
    print(s)
