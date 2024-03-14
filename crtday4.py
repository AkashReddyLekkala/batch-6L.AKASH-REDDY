# ------> While loop
# -----> break using while loop

#eg-1
# 1.) iterate from 20 to 30 and break the loop in 27
# method --->1
'''
i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1
'''
# method ----> 2
'''
i=20
while i<31:
    print(i)
    i+=1
    if i==27:
        break
'''
# method ---> 3
'''
i=20
while i<31:
    print(i)
    if i==27:
        break
    i+=1
'''
# --> only print 27
'''
i=20
while i<31:
    if i==27:
        print(i)
        break
    i+=1
'''
#  -----s> continue
#eg--1
'''
i=20
while i<31:
    if i==27:
        continue
    print(i)
    i=i+1
'''
# ---> skip the 27 number
# --> method-1
'''
i=20
while i<31:
    i+=1
    if i==27:
        continue
    print(i)
'''
# --> method-2
'''
i=20
while i<31:
    if i==27:
        i+=1
        continue
    print(i)
    i+=1
'''

# ! Eg:-3
# while to iterate from 12 to 22
# find sum of all numbers00
'''
i=12
sum=0
while i<=22:
    sum=sum+i
    i+=1
print(sum)
'''
# ! Eg-4
# Find the average of value from 20 to 25
'''
i=20
sum=0
count = 0
while i<=25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)    
'''

# ----> Nested for loop
# Eg:-1
'''
for row in range(1,3+1):
    for col in range(1,4+1):
        print(row,col)
'''
# Eg:-2
# * * * * 
# * * * * 
# * * * * 
# * * * *
'''
rows = int(input("Enter the rows : "))
cols = int(input("Enter the cols : "))
for row in range(rows):
    for col in range(cols):
        print("*" , end=" ")
    print()    
'''
# mod-->2
'''
sum = 0 
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum , end=" ")
    print()    
'''

# ! to print stars in right angled triangle
'''
for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print() 
'''
#eg-1
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
'''
for row in range(6, 0 , -1):
    for col in range(0,row):
        print("*",end=" ")
    print() 
'''
#eg-2
# * * * * *
# *       *
# *       *
# *       * 
# * * * * * 
'''
for row in range(6):
    for col in range(6):
       if col==0 or col==5 or row==0 or row==5:
            print("*",end=" ")
       else:
            print(" ",end=" ")
    print() 
'''
#eg-3 
#        *
#      * * *
#    * * * * *
#  * * * * * * *
'''
for row in range(6):
    for col in range(6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()        
'''
# eg-4
# *
# * *
# *   *
# *     *
# *       *
# * * * * * *   
'''
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
'''
# ! -----> Datatypes
# --> Primary
# --> Number ----> int,float,complex
# --> String
# --> None
# --> Collection
# --> List
# --> Tuple
# --> Set
# --> Dictionary

# ? --> List

#  1.) if the collection of elements are sorounded by square
#      brackets,it is considered to be list
# !  eg:-1
  # 1i = [4,7,9,8,89, "hello", 7+9j, [ 8,9,0]]

# characteristics of list
# 1.) list have to be sorrounded by[].
# 2.) it is mutable (the elements in the list are  chargable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) its heterogenous

#  -->eg:-1
# To acces the elements in the list
'''
l1 = [1,4,2,3,4,5,5,6,6,3,5,5,4,4,"r"]
print(l1)
'''

# ---> Indexing
# 1.) In the collection of datatypes like list,tuple,string,the
#      elements will be alloted with predefines unique values
#      called index value

# We have 2 types of indexing
# Positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side
 
# ? ----> Positive indexing
'''
lst1 = [1,4,2,3,98,5,5,6,6,3,5,5,4,4,"r"]
print(lst1[3])
print(lst1[4])
print(lst1[8])
'''

# ? ----> Negative indexing
'''
lst1 = [24,34,65,87,6,"akash","vijay","hima"]
print(lst1[-1])
print(lst1[-2])
print(lst1[-3])
'''

# ? ----> slicing
# lst1[start_index:end_index:step]
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[3:8])
print(lst1[1:4])
print(lst1[:6])
print(lst1[3:])
print(lst1[:])
'''
# --->M:-2
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[0:7:2])
'''
# ---> M:-3
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[-4:-1])
print(lst1[-1:-4])
print(lst1[-7:-1])
'''
# ---> M:-4
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[-7:-1:2])
'''
# ! To insert ot add element inside list

#append() --> used to add element at last position of list
'''
l1 = [9,80,6]
l1.append("car")
print(l1)
'''





