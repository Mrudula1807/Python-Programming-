units=int(input("Enter number of units: "))
if (units<=100):
    bill_amount=units*3.46
    print(bill_amount)
if (units>=101):
    bill_amount=units*7.43
    print(bill_amount)
if (units>=501):
    bill_amount=units*10.32
    print(bill_amount)
