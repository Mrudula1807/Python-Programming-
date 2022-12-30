x=int(input("enter the no.1:"))
n=int(input("enter the no.2:"))
choice=int(input("enter your choice:"))
if(choice==1):
    a=x+n
    print(a)
if(choice==2):
    s=x-n
    print(s)
if(choice==3):
    m=x*n
    print(m)
if(choice==4):
    p=pow(x,n)
    print(p)
if(choice==5):
    try:
        d=x%n
    except:
        print("cannot divide by zero")
    else:
        print(d)
