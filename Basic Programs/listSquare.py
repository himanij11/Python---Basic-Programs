#Squaring of element in the list
s=[4,3,2,1]
ss=[]
for i in s:
    ss.append(i**2)
print(ss)

#The above list can be performed in another way using List Comprehension:-
#List Comprehensions provide a concise way to create list.
#Common Applications are to make new lists where each element is the result of some operations applied to each member of an
#
squares=[i**2 for i in range(4)]
print(squares)

#list_name=[operations in left side///// conditions in right side]

even=[i for i in range(10) if i%2==0]
print(even)
