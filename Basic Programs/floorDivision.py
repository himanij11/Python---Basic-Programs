#Floor division (//)

a,b=9,5
c=a//b
print(c) #returns integer value


#Exponent(**)
a,b=4,2
c=a**b
print(c)

#Bitwise operators:- #returns the bit directly whereas logical operator returns 0 or 1

#AND

a,b=10,4
print(a&b) #multipication of a and b

print(a|b) #addition of a and b

#Assignment operators:-
a,b=2,3
a+=b
print(a)

a=-b
print(a)

a<<=b
print(a) #a=left shift b ,shifting occurs for 8bit

#Identity operators:-They are used to check if two values or variables are located on the same part of the memory.
a,b=5
print(a is b) #returns true or false
a,b=2,3
print(a is b) #it checks the memory location of a and b and not the values of a and b
l1=[1,2,3]
l2=[1,2,3]
print (l1 is l2) #false as it checks the memory location of l1 and l2,id(l1)and id(l2) are different.
s1="Hi"
s2="Hi"
print(s1 is s2) #true
print(s1 is not s2) #false
s3="Abc"
s4="abc"
print(s3 is s4) #false
s5="ABC"
s6="Abc"
print(s5 is s6)

#Membership operators:- They are used to test whether a value or a variable is found in sequence or not(string,list,tuple,set or dictionary)
m=[1,2,3,4]
print(1 in m) #True

d={1:"a",2:"b"}
print (1 in d) #True

lst=[1,2,3]
print(4 not in lst) #True
