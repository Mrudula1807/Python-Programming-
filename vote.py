age=int(input("enter the age of person:"))
if(age>=18):
   print("you are allowed to vote")
elif(age<18):
   print("not eligible")
   result=18-age
   print("you are allowed to vote after years:",result)
