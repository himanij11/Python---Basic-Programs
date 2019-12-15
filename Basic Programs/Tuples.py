#Tuples
#Similar to list
#Difference between them is that we cannot change the elements of tuple once it's assigned 

#tuple can be empty
t=()

#tuples having integers
t=(1,2,3)
print(t)

#tuple with mixed data-types
t=(1, 'raju', 28, 'abc')
print(t)

#Nested tuples
t=(1, (1, 2, 3), [1, 'raju', 28, 'abc'])
print(t[2])

#if there is one element always put ',' after that element so to store it as tuple
t=('satish',)
print(type(t))

#Accessing elements in tuple
t=('Raju', 1, 3, 'abc')
print(type(t))
print(t[0])

#Negative Indexing
print(t[-1])

#Nested Tuple
t=('abc', ('Himani', 'Devvrat'))
print(type(t))
print(t[1])
#To access Devvrat in Nested Tuple
print(t[1][1])

#Slicing of Tuple
t=(1, 2, 3, 4, 5, 6)

#[Include element:Excluding that element]
print(t[1:])
print(t[1:5])
#Negative Indexing
print(t[-2])

#Tuples are immutable i.e. it cannot be reassigned to existing tuple
#t=(0,1,2,3,4)
#t[2]=56

#Concatination of tuples
t1=(0,1,2,3)
t2=(4,5,6)
t=t1+t2
print(t)
#print(t1+t2)

#
t=("Himani",)
t1=(t*4)
print(t1)
#
t=(1,)
print(t*4)

#Tuple Deletion
#single Element in tuple cannot be deleted because tuple is immutable
t=(1, 2, 3, 4, 5)
del t #delete entire tuple

#Tuple index
t=(1, 2, 3, 4, 5, 3, 3, 7)
print(t.index(3)) #return value of first occurance from list

#To get maximum element from the tuple
t=(1, 2, 3, 4, 5)
print("Maximum Element from tuple :{}".format(max(t)))

#To get minimum element from the tuple
t=(1, 2, 3, 4, 5)
print("Minimum Element from the Tuple :{}".format(min(t)))

#To get Sum of Elements in the tuple
print("Sum:{}".format(sum(t)))


















