#  ! -----> Common functions for list
# Eg-1
'''
l1 = [6,7,8,9,0]
print(len(l1))
'''
# Eg-2
'''
l1 = [6,7,8,9,0]
print(max(l1))
'''
# Eg-3
'''
l1 = [6,7,8,9,0]
print(min(l1))
'''
# Eg-4
'''
l1 = [6,7,8,"t","f"]
print(max(l1)) # error coz it is combination of int and string
'''
# Eg-5
'''
l1 = [6,7,8,"t","f"]
print(min(l1)) # error coz it is combination of int and string
'''
# Eg-6
# index() --> to get index value of specific element
'''
l1=[2,34,56,65,8.57,9.64,-6]
print(l1.index(34))
'''
# Eg-7
# count() --> how many num of times an element is repeated
'''
l1=[2,34,56,65,8.57,2,2,2,9.64,-6]
print(l1.count(2))
'''

# ! some functions which is specifically used for list

# To add element inside list
# ? insert(index_value,element) --> to add element at specific index position
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.insert(2, "cars")
print(l1)
'''

# ? To delete element from list
# pop() --> last element will be deleted
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.pop()
print(l1)
'''
# pop(inde_valve) --> used to delete element at specific index
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.pop(5)
print(l1)
'''

# remove(element) --> used to delete element directly
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.remove(6.76)
print(l1)
'''
# clear() --> to complete delete all element in list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.clear()
print(l1)
'''

# del -> to delete the list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
del l1
print(l1)
'''

# ? ----> join 2 lists
'''
l1 = [9,0,4]
l2 = ["a","k","a","s","h"]
print(l1+l2)
'''

# or
# extend() --> to combine 2 lists
'''
l1 = [9,0,4]
l2 = ["a","k","a","s","h"]
l1.extend(l2)
print(l1)
'''

# --->  copy()
'''
l1 = [6,7,8,9]
l2 = l1.copy()
print(l1)
print(l2)
print(id(l1))
print(id(l2))
'''

# ! diff between shallow copy and deep copy
# shallow copy
'''
import copy
l1 = [8,9,0,[5,6],[6,4,7]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
'''

# deep copy --> used to copy with nested list
'''
import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1]) 
l2=copy.deepcopy(l1)
l1[-1].append('cars')
print(l1)
print(l2)
'''

# sort --> arrange elements in list in ascending or descending order
# Eg:-1
# M:-1 --> ascending order
'''
l1 = [9,7,2,3,5,23,63,32]
l1.sort()
print(l1)
'''
# M:-2 --> descending order
'''
l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)
'''
# Eg:-2
# M:-1
'''
l1=['v','f','e','u','a']
l1.sort()
print(l1)
'''
# M:-2
'''
l1=['v','f','e','u','a',4,3]
l1.sort()
print(l1) --> error
'''

# ? list construcyor
# list() --> to error other collection datatype to list
# M:-1
'''
l3 = ((8,9,6,0))
print(list(l3))
'''
# M:-2
'''
l4 = (56,53)
print(list(l4))
'''

# ! ----> nested list
# M:-1
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[3][1])
'''
# M:-2
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:5])
'''
# M:-3
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:-1])
'''

# ? to delete "t" from l1
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
l1[-1].remove('v')
print(l1)
'''

# ? Combine these ["p","o",'y"],[8,'t'] lists in l1 to ["p","o","y",8,'t']
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)
'''

# ! ----> Tuple
# char of tuple

# 1.) Tuple have to be surrounded by ()
# 2.) The elements inside tuple are not changable
# 3.) The elements inside tuple are indexed
# 4.) The elements will execute in order
# 5.) It is heterogenous
# 6.) It allow dupllicate elements

# Eg:1
'''
t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey",9+6j)
print(t1)
print(type(t1))
'''

# ? indexing, slicing are all same as list
# M:-1
'''
l1=(8)   # int
print(type(l1))
'''
# M:-2
'''
l1 =(8,)
print(type(l1))
'''
# M:-3
'''
t1=8,9
print(type(t1))
'''
# M:-4
'''
t2=8,
print(type(t2))
'''

# len(), min(), max(), index(), count() --> all same as list
# to add elements inside tuple --> cannot add
# cannot delete any element in tuple
# Join two tuples
# M:-1
'''
t1=(8,9,0)
t2=(11,23,32)
print(t1+t2)
'''

# To add all element inside list and tuple
#  --> sum()
'''
l1 =[8,9,7,6]
print(sum(l1))
'''

# sort tuple
# M:-1
'''
t1 = (8,9,0,89,12)
print(tuple(sorted(t1)))
'''
# M:-2
'''
t1 = (8,9,0,89,12)
print(tuple(sorted(t1,reverse=True)))
'''

# Iterate list and tuples
# Iterate based on elements
'''
l1 = [9,8,0,6,5]
for i in l1:
    print(i)
'''
# Iterate based on index value
'''
l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])
'''

# ! ----> Strings
# M:-1
'''
s1 = 'o'
print(type(s1))
'''
# M:-2
'''
s1 = "o"
print(type(s1))
'''
# M:-3
'''
s1 = "hello world"
print(s1)
'''
# M:-4
'''
s1 = "hello world"
print(s1[0:5])
'''
# To access string
# indexing and slicing --> same as list and tuple

# ---> common functions
# len(), min(), max(), index(), count()
# M:-1
'''
s1="hello world"
print(len(s1))
'''
# M:-2
'''
s1="helloworld"
print(min(s1))
'''
# M:-3
'''
s1 = "helloworld"
print(max(s1))
'''
# ord() --> used to find the ASCII value of a character
'''
s1 = 'u'
print(ord(s1))
'''

# functions of string
# ---> to convert all characters to upper case
'''
s1 = "hello world"
print(s1.upper())
'''
# ---> to convert all characters to lower case
'''
s1 = "HELLO WORLD"
print(s1.lower())
'''

# --> strip()
# --> to eliminating the space in beginnning and end of string
# M:-1
# --> to eliminate left space
'''
s1 = "   where are you.?"
print(s1.lstrip())
'''
# M:-2
# --> to eliminate right space
'''
s1 = "where are you.?  "
print(s1.rstrip())
'''
# M:-3
# --> to eliminate right and left space
'''
s1 = "   where are you.?    "
print(s1.strip())
'''

# ---> split()-->
# --> to split the words in string based on a character
# M:-1
'''
s1= "where are you.?"
print(s1.split(" "))
'''
# M:-2
'''
s1= "where are you.?"
print(s1.split("r"))
'''
# M:-3
'''
s1= "where are you.?"
print(s1.count("e"))
'''

# replace() --> to replace a specific char in the string
'''
s1= "where are you.?"
print(s1.replace('r','&&'))
'''

# swapace() --> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
'''

# title()
'''
s1 = 'nEVER gIVEUP'
print(s1.title())
'''

# capitaliez() --> 1st char of string will be converted to capital
'''
s1 = "never giveup"
print(s1.capitalize())
'''

# join the strings
'''
s1 = "hello "
s2 = "world"
print(s1+s2)
'''
# example
'''
s1 = 'how are you
i am fine
hey there'       
print(s1.splitlines())
'''

# find() --> to find the index based on a char
# M:-1
'''
s1 = "hello world"
print(s1.find('h'))
'''
# M:-2
'''
s1 = "hello world"
print(s1.index('h'))
'''

# join() -->
# M:-1
'''
l1 = ["hey","there"]
print(" ".join(l1))
'''
# M:-2
'''
l1 = ["hey","there"]
print("$".join(l1))
'''
# Example
'''
s1 = "Welcome to all"
print(s1.endswith('l'))
'''
# Example
'''
s1 = "Welcome to all"
print(s1.startswith('W'))
'''
# Example
'''
s1 = "67"
print(type(s1))
print(s1.isdigit())
'''

# Print the string in reverse manner
'''
s1 = "Welcome to all"
print(s1[::-1])
'''

# ! ---> Eg:-1
# wap to find the number of lower case letters
'''
s1 = "HEY there you ARE"
count=0
for i in s1:
    if i.islower():
        count+=1
print("The total num of lower case letters : ",count)
'''

# ! ----> Eg:2 r ---> "$"
# M:-1
'''
s1 = 'restarter'
print(s1[0] + s1[1:].replace('r','$'))
'''
# M:-2
'''
s1 = 'restarter'
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst, "$")
print(fst+txt)
'''

# ! ----> Eg:3
# m:-1
'''
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
characters = len(s1)
print(characters)
'''
# M:-2
'''
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
words  = s1.split(" ")
print(words)
'''
# M:-3
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
sentenses = s1.split('.')
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
print(len(sentenses))        



