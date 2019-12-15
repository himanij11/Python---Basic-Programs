#Magic Methods

class Employee(object):
    def __init__(self,firstname,lastname,salary=0):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary

    def __str__(self):
        return 'Full Name:' + self.firstname + ' ' + self.lastname

    #For overloading the (+)
    def __add__(self,other):
        return self.salary + other.salary
    
    #For overloading the (*)
    def __mul__(self,other):
        return self.salary * other.salary

if __name__ == '__main__':      #to use when in the same module
    Omkar = Employee('Omkar','Patil',10000)
    Amit = Employee('Amit','Patil',20000)
    print(Omkar)
    print(Amit)
    print(Omkar + Amit)     #addition of salaries
    print(Omkar * Amit)     #multipication of salaries



