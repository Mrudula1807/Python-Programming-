n=input("enter a string : ")
letter = "T"
res = len([ele for ele in n.split() if letter in ele])
print("Count of words that starts with T : " + str(res))

#other process
'''
a=input("enter the string")
def words(string):
    
   count=0
   
   for word in string:
       
       if word[0]=='T':
           
          count=count+1
          
          print(count)
words(a)
'''

'''
n = "There is a Tortoise"
print("The string is : " + str(n))
letter = "T"
res = len([ele for ele in n.split() if letter in ele])
print("Count of words that starts with T : " + str(res))
'''
