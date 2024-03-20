# ----> Constructors
# Eg:-2
'''
class profile:
    def __init__(self):
        print("Hello world")
obj = profile()
obj.__init__()
'''
# Eg:-3
# Parameterised Constructor
'''
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
obj = profile(230,"akash",20)
'''
# Eg:-4
'''
class c1:
    email = "lekkala@gmail.com"
    def m1(self): 
        name = "Akash"
        place = "Somapuram"
        print(name,place)
        print(self.email)
object = c1()
object.m1()
'''
# Eg:-5
'''
class c1:
    def m1(self):
        name = 'Akash'
        age = 20
        return name, age
    def display(self):
        print(self.m1())
object = c1()
object.display()
'''
# Eg:-6
# To use the variable inside the constructor in another methods
'''
class class1: 
    def __init__(self):
        self.name = "Akash"
        self.email = 'lekkala@gmail.com'
        #return name, email --> error 
    def display(self):
        print(self.name, self.email)
c1 = class1()
c1.display()
'''

# !------> Inheritance
# The process of utilising the methods and attributes of parent
# class throught the object of child it is called as inheritance

# 5 types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal inheritance

# ---> Single Inheritance
# It has only one parent class and only one child class
# Eg:-1
'''
class parent:
    def m1(self):
        print("I am parent class")
class child(parent):
    def m2(self):
        print("I am child class")
obj = child()
obj.m1()
'''
# Eg:-2
'''
class c1:
    def __init__(self):
        print("I am constructor from parent class")
class child(c1):
    pass
obj = c1()
'''
# Eg:-3
'''
class parent:
    name = 'Akash'
class child(parent):
    name = "hima"
    def display(self):
        print(self.name)
d = child()
d.display()
'''

# !---> Multilevel inheritance
# Eg:-1
'''
class voice:
    def sound(self):
        print("All the animals have their own voices")
class dog(voice):
    def dog_voice(self):
        print("bark")     
class cat(dog):
    def cat_voice(self):
        print("Meow")
class parrot(cat):
    def parrot_voice(self):
        print("speak")
all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''               
# Eg:-2
'''
class honda_city:
    def engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def honda_city_body_specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
class amaze(honda_city):
    def amaze_engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def amaze_city_body_specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
class civic(amaze):
    def civic_city_engine_specs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def civic_city_body_specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
class Honda(civic):
    pass
honda = Honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_city_body_specs("white",2000,5.5,8,"Hatchback")
'''

# ---> Multiple inhheritance
# It has multiple parent and 1 child
# Eg:-1
'''
class white_petrol:
    def function_w(self):
        print("used to Airplans")
class organic_petrol:
    def function_o(self):
        print("Used for Bike, Cars")        
class premium_petrol:
    def function_p(self):
        print("sport cars, bikes")       
class petrol(white_petrol, organic_petrol, premium_petrol):
    def defanation(self):
        print("Petrol types")
p = petrol()
p.defanation()
p.function_o()
'''
# Eg:-2
'''
class addition:
    def add(self, a, b):
        print(a+b)
class subract:
    def sub(self, a, b):
        print(a-b)      
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc =  division()
calc.add(3, 4)
calc.sub(6, 7)
calc.mul(5, 2)
calc.div(30, 3)
'''

# -----> Heirarical inheritance
# The one parent class will act as parent for all the child class
# Eg:-1
'''
class category:
    def weight(self,weight):
        print(weight)
    def display(self, colour, taste):
        print(colour, taste)    
class Tomato(category):
    def tomato_specs(self):
        colour = "reds"
        taste = "neutral taste"
        self.display(colour, taste)
class carrot(category):
    def carrot_specs(self):
        
        colour = "green"
        taste = "sweet"
        self.display(colour, taste)
c = carrot()
c.carrot_specs()
c.weight("30gms")
t = Tomato()
t.tomato_specs()
t.weight("20gms")
'''
# Hybrid inheritance
# The combination of above 4 inheritance is called hybrid inheritance
# Eg:-1
'''
class c1:
    def m1(self):
        print("Class 1")
class c2(c1):
    def m2(self):
        print("Class 2")
        
class c3(c2):
    def m3(self):
        print("Class 3")
class c4:
    def m4(self):
        print("Class 4")
class c5(c3):
    def m5(self):
        print("Class 5")
        
class c6(c5,c4):
    def m6(self):
        print("Class 6")
        
obj = c6()
obj.m1()
obj.m2()
obj.m3()
obj.m4()
obj.m5()
obj.m6()
'''

# ! ----> Polymorphism
# poly - many, morph --> form
# A function which has the adility to prform more than 1
# functionality that it is considersd to be as polymorphism.

# Polymorphism in built in functions
# len() --> which is used to find the length of list, tuple
# dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more..

# polymorphism in operators

# +
'''
print(8+8)
print("k" + '1')
print([1,2,3]+[5,6])
'''

# *
'''
print(4*6)
l1 = [1,2,3,4]
print(*l1)
# def f1(*args)
l1 = [1,2,3,4]
print(l1*6)
'''

# Polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading --> it is not possible in python
# 2.) Method overriding














