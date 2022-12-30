n=input("enter a string:")
vowels=0
vow=['a','e','i','o','u']
for i in n:
    if(i in vow):
    # another case optional if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("number of vowels: ")
print(vowels)
