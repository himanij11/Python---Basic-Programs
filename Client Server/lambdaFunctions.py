#'lambda' is used for creating anonymous functions!
#lambda arguments:expression
#we can have no. of arguments but we can have only a single expression
#the expression is evaluated and returned.
#lambda functions can be used wherever function objects are required.

"""
double = lambda x:x*2
print(double(5))
o/p:- 10


A=lambda x,y,z:x+y+z
A(1,2,3)
o/p:6

"""

A=lambda x,y,z:x+y+z
print(A(1,2,3))

B=lambda x,y,z:x+y+z
c=B(6,9,1)
print(c)

###############################################################################

#use with filter()
#it is used to filter the list and the o/p will be a tuple

my_list = [1,5,6,8,2,9,11]

new_list = list(filter(lambda x:(x%2==0),my_list))

print(new_list)     #o/p:[6,8,2]

#################################################################################

#use with map()

my_list=[1,5,7,9,2]

new_list = list(map(lambda x:x*2,my_list))

print(new_list)     #o/p:[2,10,14,18,4]

################################################################################


#example of map
n=int(input("Enter the no. of terms:"))
result = list(map(lambda x:2**x,range(n)))
print(result)


















