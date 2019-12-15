#Dictionary

#Syntax
#d = {Key : Value}
#print(d)

#Empty Dict
d = {}

#Dictionary with integer keys
d1 = {1: 'Himani', 2: 'Devvrat'}
print(d1)

#Dictionary with mixed key
d2 = {'Name': 'Devvrat', 1: ['Himani', 'Alen']}
print(d2)

#List of multiple tuples
d3 = dict()

my_dict = dict()
print(my_dict)

#Dictionary Access
d4 = {'Name': 'Himani', 'Age': 20, 'Address': 'Shahad'}
print(d4['Age'])

#if key is not present it will give an error
#print(d4['degree'])

#Another way to access
print(d4.get('Address'))

#if key is not present
#print(d4.get('Degree'))

#Add or Modify Elements
d5 = {'Name': 'Devvrat', 'Age': 19, 'Address': 'Kurla'}

#update name
d5['Name'] = 'Himani'
print(d5)

#add new key
d5['Degree']= 'B-tech'
print(d5)

#Delete
print(d5.pop('Age'))
print(d5)

#remove last item/arbitary key
d5.popitem()
print(d5)


#Delete a particular key
squares = {2: 4, 3: 9, 4: 16, 5: 25}
del squares[2]
print(squares)

#Remove all items from the Dictionary
squares.clear()
print(squares)

#Delete dictionary itself
del squares
print(squares) #Name error bcoz Dictionary is deleted

#











