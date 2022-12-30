n=int(input("Enter number of classes held : "))
a=int(input("Enter number of classes attended : "))
s=n/a*100 
if(a<75):
    medical_issue=input("enter yes/no if any medical issues?")
    if(medical_issue=='yes'):
            print("eligible")
    else:
            print("not eligible")
if(a>=75):
    print("eligible")
    print(s)
