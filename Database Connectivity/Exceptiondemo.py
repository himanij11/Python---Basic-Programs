#Exception Handling
#Python Errors and built in Exceptions

#1/0 #ZeroDivision Error

#open('text.txt') #IO Exception

#dir(__builtins__)

#TRY , EXCEPT AND FINALLY

"""
#import module sys to get the type of exception
import sys
lst=['b',0,2]

for entry in lst:
    try:
        print("The entry is ",entry)
        r=1/int(entry)
    except:
        print("Oops!",sys.exc_info()[0],"occured.")    #exc_info:exception information.If [0] is removed it gives detailed information.It creates an array of detail information.
        print("Next Entry.")
        print("************************************")
print("The reciprocal of",entry ,"is",r)
"""


#raise KeyboardInterrupt:- Used for raising exception by ourself


"""
try:
    num=int(input("Enter a positive integer."))
    if num<=0:
        raise ValueError("Error:Entered a negative number")   #ValueError is a class in python , we have passed "Error:Entered a negative number" in its constructor
except ValueError as e:      #we have created an object (e) of ValueError class where the string "Error:Entered a negative number" is passed in e
        print(e)
"""



"""
try:
    f=open('hello.txt')
    #perform file operations
finally:
    f.close()
"""





a=[1,'s',6,0]
try:
    for element in a:
        x = 2/int(element)
        print(x)
except Exception as e:
        print(e)
finally:
        print(a)





        
