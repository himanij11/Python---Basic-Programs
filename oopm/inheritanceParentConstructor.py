class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name," ",self.age)

class Employee(Person):
    def __init__(self,name,age,hobby):
        super().__init__(name,age)              #calling constructor of parent class
        self.hobby=hobby
    def display(self):
        super().display()       #calling method of parent class ---->MEHTOD OVERRIDING , POLYMERPHISM
        print(self.name," ",self.age," ",self.hobby)

e=Employee("Rahul",21,"Coding")
e.display()         #it will call the display method of child class

#super().display()       #gives Error because we cannot call method of parent class outside the scope of parent class
#we need to call the method of parent class in child class where the method of child class is defined

#Overloading is not supported!!!!!!!!!!!!!

#Multiple inheritance is supported!! (A Child can have multiple parents)


