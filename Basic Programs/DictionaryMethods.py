#Dictionary Methods

#Copy function:- Copies dictionary as it is to another variable
squares = {2: 4, 3: 9, 4: 16, 5: 25}
my_dict=squares.copy()
print(my_dict)

#fromkeys[seq,[,v]]  Returns a new dictionary with keys from seq and value to v

subjects={}.fromkeys(['Maths','English','Hindi'],10)
print(subjects)

subjects={2: 4, 3: 9, 4: 16, 5: 25}
print(subjects.items()) #returns a new view of the dictionary keys(key value ka tuple)

subjects = {2: 4, 3: 9, 4: 16, 5: 25}
print(subjects.keys()) #returns keys of the dictionary

subjects = {2: 4, 3: 9, 4: 16, 5: 25}
print(subjects.values()) #returns values of the dictionary

d={} #get list of all available methods and attributes of dictionary
print(dir(d)) #_on both sides then it is public , if _ is on left side then it is private
