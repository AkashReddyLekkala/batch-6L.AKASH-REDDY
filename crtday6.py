# ---> Assessment
# 1.) Python program to capitalize the first and last character of
#     each word in a string
# 2.) Input : 128
#     Output : Yes
#     128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
#    Add both l1 and l2, ans=[6, 8, 10, 12]

# ASS:-1
''''
s1=input("enter string : ")
fst = s1[0].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+lst)
'''
# ASS:-2
'''
n = int(input(" enter number : "))
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")
'''
# ASS:-3
'''
l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]
op =[]
for i in range(len(l1)):
    op.append(l1[i] + l2[i])
print(op)
'''

# ! ---------> Set

# ? characteristics of set
# 1.) Set can be created using()
# 2.) The elements inside set are not indexed
# 3.) Does not allow duplicate values
# 4.) It unordered
# 5.) Heterogenous --> accept only unmutable datatype
# 6.) Mutable or changable

# Eg:-1
'''
s1 = {9,9,89,7.76,8+7j,(8,7,5),"truck",'y'}
print(s1)
'''
# Eg:-2
'''
s2 = {5, 8, 98, [9,0]}
print(s2) # TypeError: unhashable type: 'list'
'''
# Eg:-3
# min(), max(), len()

# eg
# ? to add element inside list
'''
s1 = {8, 78, 67, 'u'}
s1.add(43)
print(s1)
'''

# update()
'''
s1 = {8,6,7,3,546,'u'}
s1.update([45,'i'])
print(s1)
'''
# ? delete element inside set
# pop() --> to delete one element randomly
'''
s1 = {8,4,85,7,5}
s1.pop()
print(s1)
'''

# remove()
'''
s1={4,54,6,3,0,2,68}
s1.remove(54)
print(s1)
'''

# discard()
'''
s1={4,54,6,3,0,2,68}
s1.discard(64)
print(s1)
'''

# clear()
'''
l1 = {}
print(type(l1)) 
'''

'''
s1 = set() # --> to create empty set
print(type(s1))
'''

'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''

# join the sets
# union() --> to combine 2 sets
'''
s1 = {9,0,8}
s2 = {9.90,"caed",'t',56}
s3 = s1.union(s2)
print(s3)
'''
# intersection() --> to get common elements inside set
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))
'''
# difference()
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
'''
# symmetric difference()
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.symmetric_difference(s2))
'''
# isdisjoit(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))

# ---> Problem:-1
'''
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}
for val in s1:
    if val in s2:
        str1 = "its joint set"
print(str1)
'''

# !---> dictionary
# Eg:-1
'''
d1 = {1:100, 'a':200, 4.5:"hello"}
print(d1)
'''
# Eg:-2
'''
d1 = {1:100, 'a':200, 4.5:"hello"}
print(len(d1))
'''

# ? char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key,value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed,
# 5.) Duplicate values are allowed
# 6.) It is unidexed
# 7.) It is ordered
# 8.) Key does nat allow mutable datatypes
# 9.) Values allow mutable datatypes

# Eg:-3
# To access elements in dictionary
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1)
'''
# To access the values
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1[1])
'''

# --> some common functions
# --> len(), min(), max()
# ---) min()
'''
d1={1:100, 2:200, 3:300, 4:400}
print(min(d1))
'''
# --) max()
'''
d1={1:100, 2:200, 3:300, 4:400}
print(max(d1))
'''
# To find min,max based on values
'''
d1={1:100, 2:200, 3:300, 4:400}
print(min(d1.values()))
print(max(d1.values()))
'''

# --> Dictionary based functions
# To add element(key and value pair)in dict
'''
d1={1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)
'''

# ? To replace a value in dictionary
'''
d1={1:100, 2:200, 3:300, 4:400}
d1[2] = "mango"
print(d1)
'''

# Delete element from dicttionary
# popitem() --> to delete last key value pair in dict
'''
d1={1:100, 2:200, 3:300, 4:400}
d1.popitem()
print(d1)
'''

# --> pop()
# 2 is the key in the dictionary
'''
d1={1:100, 2:200, 3:300, 4:400}
d1.pop(2)
print(d1)
'''

# clear(),del
# join 2 dictionary
'''
d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)
'''

# --> get() --> used to get the values from a key
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.get(90))
'''

# To print all the keys
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.keys())
print(type(d1.keys()))
'''

# To print all the values
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.values())
'''

# Iterating dictionary
# To iterate keys alone
'''
d1={1:100, 2:200, 3:300, 4:400}
for val in d1:
    print(val)
'''
# To iterate values alone
'''
d1={1:100, 2:200, 3:300, 4:400}
for val in d1.values():
    print(val)
'''
# to get both key and values
'''
d1={1:100, 2:200, 3:300, 4:400}
for key, val in d1.items():
    print(key, val)
'''

# ! Problem : 1

# 1.) Swap elements in string list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
'''
n = int(input("Enter num of times : "))
integer=[]
float_value=[]
string=[]
for val in range(n):
    value = eval(input("Enter the values : "))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_val.append(value)
    elif type(value)==str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
'''             
# ! Problem : 2
# M:-1
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
l1=set1^set2
print(l1)
'''
# M:-2
# return a set elements present in set A or B, but not both
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)
'''

# ! ---> Problem : 3
'''
l1 = [1,2,3,4] # key
l2 = ["a", "b", "c", "d"] # value
l1.(l2)
print(l1)
'''



















