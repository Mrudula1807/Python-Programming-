a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
discriminant=b**2-4*a*c
sqrt_root = discriminant ** 0.5
print(sqrt_root)

if discriminant>0:
    print((-b+sqrt_root)/2*a)
    print((-b-sqrt_root)/2*a)
elif discriminant==0:
    print(-b/2*a)
else:
    print("no roots")
