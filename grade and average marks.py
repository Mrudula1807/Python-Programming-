sub1=int(input("Enter marks in obtained in subject 1:"))
sub2=int(input("Enter marks in obtained in subject 2:"))
avg_marks=(sub1+sub2)/2
print("Average marks:",avg_marks)
if avg_marks>=90:
    print("Grade is A")
elif avg_marks>=80:
    print("Grade is B")
elif avg_marks>=70:
    print("Grade is C")
else:
    print("Grade is F")
