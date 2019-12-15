#Operations on the Set
#Indiabigs######Site for learning coding


#Union
set1={1, 2, 3, 4}
set2={5, 6, 7, 8}
print(set1 | set2) #OR operator '|' unions the set
#Another way
#Using Union Operator
print(set1.union(set2))

#Intersection on the set
s1={1, 2, 3, 4}
s2={4, 5, 6, 7}
print(s1 & s2) #And operator '&' intersects common values from both set
#Another way
#Using Intersection Operator
print(s1.intersection(s2))

#Difference on the set
s1={1, 2, 3, 4, 5}
s2={4, 5, 6, 7, 8}
print(s1.difference(s2))
#Another way
print(s1-s2)

#Symmetric Difference on the set 
s1={1, 2, 3, 4, 5}
s2={4, 5, 6, 7}
print(s1^s2)
#Another way
print(s1.symmetric_difference(s2))

#Subset
x={1, 2, 3, 4, 5, 6}
y={4, 5, 6}
print("Set x is subset of y? : ", x.issubset(y))
print("Set y is subset of x? : ", y.issubset(x))




























