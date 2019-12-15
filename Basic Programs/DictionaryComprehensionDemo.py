#Dictionary is unordered 
#Dictionary Comprehension
d={'a':1,'b':2,'c':3}
for pair in d.items():
    print(pair)

    
d={'a':1,'b':2,'c':3,'d':4,'e':5}
new_d={k:v for k,v in d.items() if v>2}
print(new_d)

#we can also perform operations on the key value pairs
d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
d={k + 'c':v*2 for k,v in d.items() if v>2} #we can also add special characters($,*,#,@,!) instead of 'c'
print(d)
