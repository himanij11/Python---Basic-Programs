#creating various types of list
empty=[]
print(empty)
lst=['one','two','three'] #list of strings

lst2=[1,2,3,4] #list of integers

lst3=[[1,2],[3,4]] #list of lists,a[0]=[1,2] and a[1]=[3,4]

lst4=[1,'abc',2,1.5,[4,5]] #list of different datatypes
print(lst4)

#list length

lst2=[1,2,3,4]
print(len(lst2))
a=len(lst2)
print(a)

#operations in list:-

#list append :- it adds item at the end of the list.
#syntax:- list.append()

lst=['one','two','three']
lst.append('five')
print(lst)


#list insert:-it adds an element at a given location.
#syntax:-lst.insert(position,element)
lst1=['one','two','three','six']
lst1.insert(3,"four")
print(lst1)


#list remove:-
#syntax:-lst.remove(x)
lst3=['one','two','three','two']
lst3.remove('two') #it will remove first occurence of 'two' in a given list
print(lst3)


#list append and extend:-
lst56=['one','two','four']
lst57=['three','six']
lst56.append(lst57)  #it will add lst57 as a single element to list56
print(lst56)

lst53=['one','two','four']
lst54=['three','six']
lst53.extend(lst54) #extend will join the list53 with list54(elements of lst54 will be separated and the added to lst53)
print(lst53)

#delete list:-
lst11=['one','two','three','four','five']
del lst11[1] #it will delete second element
print(lst11) 

a=lst11.pop(1) #pop is a function whereas delete is a keyword,pop will first return the element and then delete the element
print(a) 
print(lst11)

#list related keyword in python
#We can use 'in' and 'not in' in if else condition also
lst12=['one','two','three','four','five']
if 'two' in lst12:
    print("AI")
if 'six' not in lst12:
    print("MI")


#list reverse:-
#syntax:- listname.reverse()
lst13=['one','two','three','four','five']
lst13.reverse()
print(lst13)


#list sorting:- sorted(listname)function
#the original list is not changed.
#it takes a list and returns a new list with those elemenst in sorted order.
#we cannot compare string in a list.

list=[1,5,9,2,4,8]
sorted_lst=sorted(list)
print("Sorted list:",sorted_lst)
print("Original list is:",list)

b=[3,2,11]
b.sort() #sorting occurs in b , original list i.e.b changes.
print(b)

#sorting a list in descending order
list1=[1,5,9,2,4,8,11]
print("Reverse sorted list is:",sorted(list1,reverse=True))

a=sorted(list1,reverse=True)
print("Reverse sorted list is:",a)


print("Ascending sorted list is:",sorted(list1,reverse=False))


#list having multiple references
lst14=[1,2,3,4,5]
abc=lst14 #here id(lst14) and id(abc) are same
abc.append(6)
print("Original list is:",lst14)

#string split to create a list
s="India is my country"
lst=s.split()
print(lst)

s="India,is,my,country"
lst=s.split(",")
print(lst)

s="India is my country"
lst=s.split(",")
print(lst)

#list indexing
lst69=[1,2,3,4]
print(lst69[1])
print(lst69[-1])

#List Slicing
#Syntax
#list_name[starting point:end-1]
lst70=[1,2,3,4,5,6,7]
print(lst70[0:4])

#List Slicing1
#Syntax
#list_name[::skipping by no.]
#eg
lst71=[1,2,3,4,5,6]
print(lst71[::2])

#List Slicing1
#Syntax
#list_name[starting::skipping by no.]
#eg
lst72=[1,2,3,4,5,6]
print(lst72[2::2])


