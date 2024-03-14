#eg-2
#Take values of length and breadth of a from user and check if
# ! it is square or not.
'''
length=int(input("Enter the  length value : "))
breadth=int(input("Enter the breadth valve : "))
if length==breadth:
            print("it is square")
else:
    print("it is not square")
'''
#eg-3
# Python program to check whether the given integer ia s multiple
# ! of both 5 and 7
'''
a=int(input("Enter the number : "))
if a%5==0 and a%7==0:
    print("the number is multiple of 5 and 7")
else:
    print("the number is not multiple of 5 and 7")
'''
#eg-4
# Write a program to accept the cost price of a bike and dispaly
# ! the road tax to be paid.
# accordint to the following criteria:
#       cost price(in Rs)              tax
#       > 100000                       15% + discount 6% 
#       < 100000               5%
'''
price=int(input("Enter the cost of bike : "))
if price>=100000:
    discount = price*(6/100)
    value=price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax= price*(5/100)
    total = price*tax
print("The on road cost of bike is : ",total)    
'''
# if elif
# eg-1
'''
a=int(input("Enter thea A value : "))
b=int(input("Enter the B value : "))
c=int(input("Enter the C value : "))
if a>b and a>c:
    print("A is greater ")
elif b>c and b>a:
    print("B is greater ")
else:
    print("C is greater ")
'''
#eg-2
# A school has following rules for grading system:
#a.Below 25 - F
#b. 25 to 45 - E
#c. 45 to 50 - D
#d. 50 to 60 - C
#e. 60 to 80 - B
#f. above 80 - A
# ask user to enter marks and print the corresponding grade.
'''
marks=int(input("Enter the marks : "))
if marks<25:
          print("F")
elif marks>=25 and marks<=45:
    print("E")
elif marks>45 and marks<=50:
    print("D")    
elif marks>50 and marks<=60:
    print("C")
elif marks>60 and marks<80:
    print("B")
else:
    print("A")
'''
# ! ---> short hand if else
#eg-1
'''
a=9
b=60
if a>b:
    print("A")
else:
    print("B")
'''

#?---> Rules
#  1) statement inside the if condition have to be present at first
#  2) elif cannot be used in short hand if else
#  3) Always it have to end with else
# ! print("A") if a>b else print("B")

# code to check the given char is vowel or consonent
'''
char=input("Enter the char : ")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("it is vowel")
else:
    print("consonant")
'''
#              (or)
'''
char=input("Enter the char : ") 
str1= "aeiou"
if char in str1:
    print("vowel")
else:
    print("consonasnt")
'''
# ! shorthand if else
'''
char = input ("Enter the char : ")
str1 = "aeiou"
print("vowels") if char in str1 else print("consonent")
'''
# !---> elif ladder using short hand if else
# eg:1
# find greatest among  3 variables using short hand if else
'''
a=int(input("Enter thea A value : "))
b=int(input("Enter thea B value : "))
c=int(input("Enter thea C value : "))
print("A is greater") if a>b and a>c else print("B is greater")if b>a and b>c   else print("C is greater")
'''

# ! --------> looping
# looping can be implimented using
# for loop
#  while loop

# !----> for loop
#----> for loop is used for iteration,if we know the number of
#   times the loop have to run .
#------> It is used to itrate the iterables
#---> eg:--> (string,list,tuple,...etc)

#todo----> Syntax for loop

#  for syntax in C program
#  for(i=0;i<10;i++){
#        printf("hello")
#}

# ! for syntax in python
#   for userdefined_variable in range(start,end,step):
#    statement
#    statement    
#    statement

#eg:1
#To print the value from 1 to 10 using for loop
'''
for i in range(0,100):
    print(i)
'''
#eg:-2
'''
for val in range(23,50,5):
    print(val)
'''
#eg-3
# --> to decrement the value
'''
for val in range(10,0,-1):
    print(val)
'''
#eg:-4
# ! print the output of 7th multiplication table from 21 to 43
'''
for i in range(1,11):
    print('7 x', i , '='  ,i)
'''
# method-2
'''
for i in range(1,11):
    ans="7 x {} = {}"
    print(ans.format(i,i*7))
'''
# method-3
'''
for i in range(1,11):
    print(f"7 x {i} = {i*7}")
'''
# ? eg:-5
# !---> break -->= used to terminate the loop
'''
for val in range(1,10):
    if val == 7:
        break
    print(val)
'''
# eg:-6
'''
for val in range(1,10):
    print(val)
    if val == 7:
        break
'''
# eg:-7
'''
for val in range(1,10):
    if val == 7:
        print(val)
        break
'''
# ! ---> continue
# eg:-1
'''
for val in range(1,10):
    if val == 7:
        continue
    print(val)
''' 
# ! Practise problems
#--> Print the even numbers between 20 to 40
# method-1
'''
for i in range(20,41,2):
    print(i)
'''
#method-2
'''
for i in range(20,41):
    if  i%2!=0:
        print(i)
'''

# ! -----> while loop
# while is used when ew do not know the number of times the loop
# have to run to literate the non iterable elements while loop
# is used

# todo syntax
# intialisation
# while condition
#  statement
#  incre or decre
 #eg:-1
# to itearte number from 1 to 10
#eg-1
'''
i=0
while i<11:
    print(i)
    i+=1
'''
#eg-2
# to decrement using while loop
'''
i=10
while i>0:
    print(i)
    i-=1
'''
#   1------>1-4+9-16+25=15
'''
n= int(input("enter number : "))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2!=0:
        sum=sum+sq
    else:
        sum=sum-sq
print(sum)
'''
# for loop practise
#-----> Assessment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
#     numbers that fall between 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
#     n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432

















