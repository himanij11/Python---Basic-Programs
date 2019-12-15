#####Encapsulation#####

class Person():
    def __init__(self, name):
        self.name = name
        self.__education = 'Engineering'    #Private variable

    def displayInfo(self):
        name = self.name
        education = self.__education
        print('My name is ', name, 'and I completed my ', education)

myObj = Person('Omkar')
myObj.displayInfo()
print(myObj.name)                   #Can be accessed
#print(myObj.__education)            #Throws an error 
print(myObj._Person__education)     #Private variable is accessed like this




