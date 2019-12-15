#File Handling
#We can create any type of file
#open function () :-

#f=open('example.txt')  #FileNotFound Error

import os
print(os.getcwd())
f=open('example1.txt','w') #creating a new file using write mode
f.write("Hey!\n")
f.write("This is our first file.\n")
f.close()

#it will give ValueError as we have not opened the file.
'''f.write("This file contains two lines.\n")
f.write("End!\n")'''

import os
print(os.getcwd())
f=open('pythonfile.py','w')
f.close()

f=open("new.txt",'w')
f.write("India is my country")#if we dont write f.close() it prints the no. of characters
f.close()
f=open('new.txt','r')
f.read()
f.close()


#f.read() or f.readline() #to read a file

f=open('newpdf.pdf','w')
f.write("Hi!\n")
f.write("This is our first pdf file")
f.close()
 



#f.tell() #it returns our current position(in number of bytes)
#f.seek() #bring the file cursor to initial position


import os
#Rename a file from new.txt to new1.txt
#os.rename("filename","newfilename")
os.rename("new.txt","hi.txt")
f.close()

#delete a file
os.remove("hi.txt")
f=open('hi.txt')



