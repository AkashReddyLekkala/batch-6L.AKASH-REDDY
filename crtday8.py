# ! Eg:-3
'''
def profile(name,age,place):
    txt = "\nMy name is {}. \nI am {} years old. \nI am from {}."
    print(txt.format(name,age,place))
profile("akash", 24, "somapuram")    
'''
# Eg:-4
# ? Function with return statement
'''
def f1():
    z=8
f1()
print(z)  # error --> cannot use outside the function
'''
# ! return
# 1.) A variable declared inside the function can be accessed
#     outside the function using return
# 2.) return does not prrint anything
# 3.) we cannot write any code below return statement
# Eg:-5
'''
def f1(a,b):
    c = a*b
    return c
# print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)
def gracemark(object):
    print(object)
gracemark(obj)
gracemark(obj1)
'''
# Eg:-6
# 123 --> write a palindrome ocde
'''
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "is a Palindrome")
    else:
        print(n, " is not palindrome")
a = int(input("Enter the value : "))
palindrome(a)
'''

# ? Based on the declaration of parameter and args
# ? functions are divided into 5 catageries

#  Positional args
#  Keyword args
#  Default args
#  Variable length args
#  Keyword variable length args

# ---> Positional args
# --> The position of parameter have to be same as position as
#     arguments
# Eg:-1
'''
def profile(name, phone, mark):
    txt = "\nMy name is {}.\nMy phone number is {}.\nI got {} marks."
    print(txt.format(name, phone, mark))
profile("akash", 9652572870, 99)    
'''

# ---> Keyword args
# --> To overcome the disadvantage of position args, we use keyword
#     args
# --> It is the process of initialising the parameter with the
#     args while calling the function
# Eg:-1
'''
def profile(name, phone, mark):
    txt = "My name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name, phone, mark))
profile(name="akash", mark=99, phone=9652572870) 
'''

# todo --> Exception of keyword args function
'''
def profile(name, phone, mark):
    txt = "My name is {}.My phone number is {}.I got {} marks."
    print(txt.format(name, phone, mark))
# profile(name="akash", 9652572870, mark=99)  # error  
# profile(9652572870, name="akash", mark=99)   # error
profile("akash", phone=9652572870, mark=99) 
'''

# ---> Default args
# --> The method of assigning the argument to the parameter while
#     declaring the function
#  Eg:-1
'''
def profile(name, phone, place="Somapuram"):
    txt = "\nMy name is {}.\nMy phone number is {}.\nI am from {}."
    print(txt.format(name, phone, place))
    if place=="Kadapa":
        print("The location is matched")
    else:
        print("The location is unmatched")
profile("akash", 9652572870,"kadapa")
'''
# ---> Variable length args
# --> To pass more than 1 arg to a parameter means we use variable
#     length args
# --> To convert normal parameter to variable length parameter,
#     add * to ther prefix of parameter.
# Eg:-1
'''
def profile(*name):
    for val in name:
        print("My name is",val)
profile("akash", 'himavanth', 'vijay')
'''
# Eg:-2
'''
def profile(age,*name):
    for val in name:
        print("My name is",val, "My age is",age)
profile(20,"akash",'vijay','himavanth')        
'''

# ---> Keyword variable length args
# kwargs --> Which is used to provide the args in the form of key
#            value pair.
# Eg:-1
'''
def price(**price_list):
    print(price_list)
price(shirt = 1000, iphone = 800000)    
'''
# Eg:-2
'''
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)
'''

# -----> Assessement
# 1.) Write a Python script to generate and print a dictionary
#     that contains a number (between 1 and n) in the form
#     (x, x*x).Sample Dictionary ( n = 5) :
#     Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# 2.) Find the uncommon words from 2 strings
#    s1 = "Hello how are you"
#    s2 = "Hello how is"
# 3.) Wrire a code print the 8th fibanochi number

# ------> Answers
# 1.) Write a Python script to generate and print a dictionary
#     that contains a number (between 1 and n) in the form
#     (x, x*x).Sample Dictionary ( n = 5) :
#     Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ----> Code
# -> M:-1
'''
n = int(input("Input a number: "))
d = dict()
for x in range(1, n + 1):
    d[x] = x * x
print(d)
'''
# -> M:-2
'''
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val **2
    print(d1)
dict1(5)
'''
# 2.) Find the uncommon words from 2 strings
#    s1 = "Hello how are you"
#    s2 = "Hello how is"
# ---> Code
'''
def uncommon_words(s1, s2):
    A = set(s1.split())
    B = set(s2.split())
    uncommon = list(A.symmetric_difference(B))
    return uncommon
s1 = "hello how are you"
s2 = "hello how is"
uncommon = uncommon_words(s1, s2)
print(uncommon)  
'''
# 3.) Wrire a code print the 8th fibanochi number
# --> Code
'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
n = 8
result = fibonacci(n)
print(f"The {n}th Fibonacci number is:", result)
'''

# !------> Object oriented programming
# The panadigms of objects oriented progarmming are
# Class
# Objects
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation

# ! Class is a blue print of an object
# Eg:-1
'''
class c1:
    name1 = 'Akash'
    print(name1)
'''
# Eg:-2
'''
class person:
    name = "Prabhas anna"
c = person()
print(c.name)
'''
# Eg:-3
# create of a method
# When the function is created with a class is called as method
'''
class person:
    def display():
        print("Hello welcome to classes")
p = person()
p.display()
'''
# Eg:-4
# ! Method with parameter
'''
class person:
    def display(person, name, age):
        print(name,age)
p = person()
p.display("akash",20)
'''
# Eg:-5
'''
class person1:
    fname = "Akash"
    lname = "Reddy lekkala"
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p = person1()
p.first_name()
p.full_name()
'''
# Eg:-6
# Constructors ---> __inti__()
# This is a special method which has the ability to execute it
# self without calling it manullay through the process of
# instantiation
'''
class profile:
    def __init__(self):
        print("hey shetty ")
p = profile()
'''











