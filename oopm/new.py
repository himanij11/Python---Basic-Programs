class Demo :
    '''This is a python class'''
    a=2
    def func(self):         #self is always considered as an argument!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("Hello")


print(Demo.a) #when we define a class,a new class object is created with the same class name
print(Demo.__doc__) #It is used to fetch the docstring of that class

#__variable__ is a public and built-in variable!


#Create an object in python

b=Demo()
b.func()
print(b.a)

###################################################################

import random
class Vehicle :
    #class methods/attributes
    def type(self):
        #this is not a class attribute as the variable is blinded to self.
        #hence it becomes an instance variable
        self.randomValue = random.randint(1,10)     #setting the instance variable
car=Vehicle()   #creating an instance,if we print this object it gives the address which is a hexadecimal number.
car.type()
print(car.randomValue)

demo=Vehicle()
demo.type()
print(demo.randomValue)
################################################################




#__init__ ---> Constructor in python

class vehicle ():
    def __init__(self):     #called automatically hence known as a magic method
        #init is used to set values as soon as new object is created
        print("Calling constructor i.e.__init__")
        self.val=0
        self.cost=10000     #setting the default value when the object is created

    def incrementVehicle(self):
        self.val +=1

car=vehicle()   #__init__ is called
print('First obj value:',car.val)
car.incrementVehicle()
car.incrementVehicle()
print('First obj value after incrementing:',car.val)

bike=vehicle()   #__init__ is called which makes val=0 for this ANOTHER instance
print('First obj value:',bike.val)
bike.incrementVehicle()
bike.incrementVehicle()
print('First obj value after incrementing:',bike.val)

##############################################################################
