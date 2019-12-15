#Set is unordered collection of list of items.
#Sets are mutable
#Every element in set is Unique(No duplicates)
#Used to perform Mathematical operations
#Set doesn't support Indexing i.e. s[1] is not valid
#Set displays elements in ascending ordered list
#eg s={4, 3, 2, 1}
#print(s)
#o/p: {1, 2, 3, 4}

#set of Integers
s={1, 2, 3}
print(type(s))
print(s)

s={1.2, 6.9}
print(type(s))
print(s)

#Set doesn't Allow Duplicate Elements
s={1, 2, 3, 1, 2}
print(s)

#To cast List into Set
l=[1,2,3,4,5,6,1,2,4]
s=set(l)
print(s)

#We can create a empty set
s=set()
print(type(s))
a={}   #We need the above funcction to convert into set
print(type(a))

#Addition of Element in a set
s={1, 2, 3, 4}
s.add(5)
print(s)

#To add Multiple Elements in the Set
s={1, 2, 3, 4}
#Elements cannot be added directly in set
#It can be added as a itterable object such as Tuple, Set, Dictionary and List
s.update([7, 6, 0])
print(s)
s.update((9,8,10))
print(s)
s.update({12, 11, 13})
print(s)

#Remove Elements from the Set
s={1, 2, 3, 4, 5}
s.discard(4)
print(s)

#Discard will not give any type of error if you want to delete element which is not in the list but remove gives errors
#Another method to remove Elements from the Set
s={1, 2, 3, 4, 5, 6}
s.remove(5)
print(s)

#Pop method deletes random element from the set
s={1, 2, 3, 4, 5}
s.pop()
print(s)

#Clear function removes all elements from the set
s={1, 2, 3, 4}
s.clear()





































