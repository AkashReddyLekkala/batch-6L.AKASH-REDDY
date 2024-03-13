#variables
#eg
'''
a=7,8
print(a)
print(type(a))
'''
#eg
'''
a, b, c = 9, 8, 7, 8
print(a,b,c)
'''
#eg
'''
a, b=c=7,8
print(a)
print(b)
print(c)
'''
#eg
'''
a=b, c= 4,2
print(a,b,c)
'''
#---> swapping of variables
#eg-1
'''
a=7
b=5
temp=a
a=b
b=temp  
print(a,b)
'''
#eg-2
'''
a=2
b=4
a=a+b 
b=a-b  
a=a-b  
print(a,b)
'''
#eg-3
# its only on python
'''
a=4
b=6
a,b=b,a
print(a,b)
'''
#eg-4
'''
a=4
b=6
a=a*b
b=a/b
a=a/b
print(int(a),int(b))
'''
#eg-5
#  id()---> used to find the memory address of the variable
'''
a=7
b=8
print(id(a))
print(id(b))
'''
# ---> keywords
# keywords  are reserved words which provides special meaning to compiler or interpertor
'''
import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
print(len(keyword.kwlist))
'''
# To check if the string is keyword or not
#print(keyword.iskeyword("sid"))
'''
if =8
print(if) # error coz is a keyword
'''
# !---> literals
# Literal is the constant value assigned to a variable
# A variable is considers to be constant when it is defines
# In caps
#a=78  # a is avariable
#A=78   # A is constant
'''
l1 = [6, 7, 8, 0]
L1=89
print(l1)
'''
# hash()--> it creates a hash value for constant datatypes amd
# provides error for non constant datatypes
'''
n1 = 89+7j
print(hash(n1))'''
'''
f1 = [7,8,9]
print(hash(f1))
'''
# ---> Operaters
# Operaters are symbols which is used to perform various operations
# between  two or more operands
#-1)ARITHAMATIC
#-2)ASSIGNMENT
#-3)LOGICAL
#-4)RELATIONAL or COMPARISON
#-5)BITWISE
#-6)IDENTITY
#-7)MEMBERSHIP
# TODO----> Arthmatic ---> +,-,*,/,%,//,**
#eg-1
'''
a=2
b=6
c=6
print(a+b+c)
'''
# input()---> used to get the runtime input
# eval()--> used to get the runtime values of all datatypes
'''
n1= eval(input("Enter the value: "))
print(type(n1))
'''
#eg-2
'''
a=4
b=2
print(a/b)   # it gives quotient value
print(a%b)   # it givve remainder value
'''
# // --> floor devision
#eg-1
'''
a= 765433
b=19
print(a/b)
'''
#! **--> used for power of a number
#   print(2**4) # --> 16

# ! Assigment operater---> +=,-=,/=,//=,&=
#eg-1
'''
a=8
a+=87
print(a)
'''
#eg-2
'''
a=10
a-=4
print(a)
'''

# ! Comparison --> ==, >, <,!=,
#eg-1
'''
a=8
b=7
print(a<b)
'''
#eg-2
'''
a=6
b=6
print(a==b)
'''

# ! Bitwise operater  --> &,|,^,~,<<,>>
#eg-1
'''
a=4
b=7
print(a&b)
'''
# 2^4 2^3 2^2 2^1 2^0
#  16  8   4   2   1
#  --------------------
#   0  1   0   0   0 --> = 8 
#   0  0   1   1   1 --> = 7
#   0  0   1   1   0 --> = 6
#   0  0   1   0   1 --> = 5
#   0  0   1   0   0 --> = 4
#   0  0   0   1   1 --> = 3
#   0  0   0   1   0 --> = 2
#   0  0   0   0   1 --> = 1

#eg-2
'''
a=5
b=7
print(a|b)
'''
# ~---->
'''
a=654
print(~a)
'''
# print(16>4)
# Logical operater ---> and, or, not
#eg-1
'''
a=6
print(a>4 and a<=6)
'''
#eg-2
'''
a=6
print(a<2 or a>5)
'''
#eg-3
'''
a=7
print(not(a>8 and a<8))
'''
# shifting operater
'''
print(12<<5)
'''
# ! Identity operater
# It is used to compare the memory location where value is stored
# is , is not
#eg-1
'''
a=9
b=98
print(a is b)
'''
#eg-2
'''
a = [1,2,3]
b= [1,2,3]
print( a is b)
'''
#eg-3
'''
a = (1,2,3)
b= (1,2,3)
print( a is b)
'''
#eg-4
''''
a = [1,2,3]
b= [1,2,3]
print( a is not b)
'''
# !---> Membership operater
# ! in, not in
'''
l1 = [2,4,6,6,45,65,75]
num =eval(input("Enter the number : "))
print(num in l1)
'''
# ! conditional ststement
# if, elif, else
#eg-1
#  --->
'''
a=6
if a:
    print("Hello world")
 '''   
#eg-2
'''
a=1
if a>3:
    print("hey")
else:
    print("no")
'''
#eg-3
'''
if 7>8:
    print("yes")
else:
    print("no")
'''
#eg-4
'''
a=0
a=None
a=False
a=""
if a:
    print("yes")
else:
    print("no")
'''

# a number is even or odd
'''
a=int(input("Enter the number : "))
if a%2==0:
      print("even")
else:
      print("odd")
'''
# name, age, nationality
#18 above, indian
name=input(" enter name : ")
nation = input("enter nationality : ")
age=int(input("enter the age : "))
if age>=18 and nationality=="indian":
    print(" eligible")
else:
    print("not eligible")









