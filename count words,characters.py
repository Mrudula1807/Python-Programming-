n=input("enter a string : ")
char=0
word=1
for i in n:
    char=char+1
    if(i==' '):
        word=word+1
print("The words in the string:")
print(word)
print("The characters in the string:")
print(char)
