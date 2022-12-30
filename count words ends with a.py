n=input("Enter a string : ")
def words(string):
    count=0
    for word in string.split():
        if word.endswith("a"):
            count=count+1
    print(count)
words(n)
