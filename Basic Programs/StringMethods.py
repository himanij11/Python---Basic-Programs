#String Methods

#Lower Function
a="HIMANI"
print(a.lower())

#Split Function
a="This is a laptop"
print(a.split())

#Remove Function
a="This is a laptop".split()
a.remove("laptop")
' '.join(a)
print(a)

b="My name is Devvrat! :)".split()
b.remove("name")
' '.join(b)
print(b)

#Find Function
print("Himani Joshi".find("Hi"))

#Replace Function
s1="Bad Morning"
#.replace("Element which has to be replaced", "Element to be replaced")
s2=s1.replace("Bad", "Good")
print(s1)
print(s2)

#Reverse a String
myString="Devvrat"
myString=myString.lower()

#RevString=reversed(myString)
#Reverse string to be converted to list before displaying

print(myString)
#print(list(RevString))

"""if list(myString) == list(revString):
    print("Given String is Pallindrome")
else:
    print("Given String is not Pallindrome")"""


#Sort Words in Alphabetical Order
myString="Himani lives in Shahad"

words=myString.split()
words.sort()

for i in words:
    print(i)
























