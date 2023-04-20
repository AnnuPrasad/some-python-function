marks = [5, 6, 9, 'harry', True]
marks.append("annu")
print(marks[-3])
if 'arry' in 'harry' :
    print ("yes")
else:
    print("no")
print(marks[:])


# # #list comprehensive
lst = [i*i for i in range(10) if i%2==0]
print(lst)

# # #tuple
tup = (1, 5, "he", "she", True)
tup2 = tup[1:3]
print(tup2)
# # #convert tuple into list for changes:
temp =list(tup)
print(temp)


# #f string function:
# country = str(input())
# name = str(input())
# print(f"hello i am from {country} and i am {name}")


#Recursive method (function call itself)
def facto(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*facto(n-1)
print(facto(4))





#Set and its methods (set does not take repeted value)
        #union method
s = {2,4,2,6} #set
s1 = {21,41,21,6}
print(s.union(s1)) #union in set
# s.update(s1)          #it update the value of s and include all vale of s1
print(s)
        #intersection and intersection update
cities1 = {"seoul", "delhi", "tokyo", "madrid"}
cities2 = {"seoul", "delhi", "berlin", "madrid"}
cities4 = {"seoul", "delhi", "berlin"}
cities3 = cities1.intersection(cities2) #intersection of cities1 and 2
#cities1.intersection_update(cities2)
#cities3 = cities1.symmetric_difference(cities2)    #method for symmetric difference
#cities1.symmetric_difference_update(cities2) #show the set(A)-set(B)
print(cities3)

#disjoint set
print(cities1.isdisjoint(cities2))
print(cities1.issuperset(cities2)) # check superset
print(cities4.issubset(cities2)) #check subset

#add, remove and discard single item to set 
cities1.add("hong kong")
print(cities1)
cities1.remove("tokyo") 
#cities1.discard("tokyo2") #it through does not through error when we run it while remove does 
print(cities1)

item = cities1.pop() #it pop random value in set
print(item)

#del cities1
cities1.clear() #del delete the entier set while clear delete item in set and set become empty
print(cities1)





#DICTIONARY IN PYTHON (it create a mapping of objects)
info = {'name':'karan', 'age':19, 'eligible':True}
print(info)
print(info['name'])# FOR PIRTICULAR VALUE 
print(info.get('name'))#IF YOU WANT TO THROW error IN PROGRAMME THAN USE info() FOR VALUE WHICH IS NOT exist IN DICT OTHERWISE USE info.get()
print(info.keys())
print(info.values())
    #ACCESS OF DICT OBJECT
for key in info.keys():
    print(info[key]) #IT ITERATE ALL THE KEY IN DICT 
for key in info.keys():# for value and key 
    print(f"the value corresponding to the key {key} is {info[key]}")# by using f string
print(info.items())
# for key, value in info.items(): #items() gives key value pairs
#     print(f"the value corresponding to the key {key} is {value}")

#some method in dict
#update()
#clear()
#pop() #to remove a key-value pair
#popitem() #to remove last item in key-value pair
#del()  #to delete key and dict





#FOR LOOP with else
for i in range(6):
    print(i)
    if i==4:
        break #it break the loop
else:
    print("sorry")# else is execute when loop is finished. If else os not executed then loop is break 




# ERROR HANDLING
m = input("Enter a number ")

try:
    print(f"multiplication of table {m} is: ")
    for i in range(1,11):
        print(f"{int(m)} X {i} = {int(m)*i}")
except:
    print("invalid input")

print("End of the programme")
#specific exception handling example:
try:
    numb = int(input("enter an integer "))
except ValueError:
    print(f"ther value is not an integer.")
print("programme END")
##FINALLY KEYWORDE
def fact(n):
    
    try:
        if (n==0 or n==1):
            return 1
        else:
            return n*fact(n-1)
    except:
        print("some error occured")
        # return 0
    finally:
        print("iam always executed")
n = int(input())
x= fact(n)
print(x)





#short-hand if else:
a = 3309
b = 3303
print("A") if a>b else print("=") if a==b else print("B")
c = 9 if a>b else 0  #you also print expression by this method
print(c)
#it reduce readibility of the code and not suitable for complex code



# Enumerate function = it increase the index number in a loop
marks = {54, 65, 98, 96, 88}
for  index, mark in enumerate(marks, start = 1): #start value is where to start  index number
    print(mark)
    if (index == 3):
        print("Awesome")



#lamda function
#two ways to use lamda function
name = lambda x: x*2
print(name(5))

