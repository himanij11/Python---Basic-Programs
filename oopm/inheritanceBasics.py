class Employee():
    def __init__(self,designation,iD,name,salary):      #class variable
        """
        What the class should do when it is             #doc_string
        used to create an instance.
        """
        self.designation=designation    #scope of class
        self.iD=iD
        self.name=name
        self.salary=salary

#constructor is used for intialising and assigning different values to objects
        
e1=Employee("Manager",10,"Rohit",50000)     #creating object and invoking the constructor
e2=Employee("CEO",20,"Naveen",100000)       #local variable
e3=Employee("Teacher",30,"Mahesh",60000)
e4=Employee("Engineer",10,"Rajesh",75000)

print(e1.designation,e1.iD,e1.name,e1.salary)
print(e2.designation,e2.iD,e2.name,e2.salary)
print(e3.designation,e3.iD,e3.name,e3.salary)
print(e4.designation,e4.iD,e4.name,e4.salary)

#################INHERITANCE###########################################

class Manager(Employee):        #()-->indicates the parent class
    year_of_joining=2018        #creating a variable of child class

e=Manager("General Manager",285,"Mohak",50000)  #creating an object of child class
print(e.designation,e.iD,e.name,e.salary,e.year_of_joining)

#super is used to call parent constructor




