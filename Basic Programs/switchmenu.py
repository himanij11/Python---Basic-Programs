a=2
b=3
print("1.Addition\n2.Subtraction\n3.Multiplication")
"""
print("2.Subtraction")
print("3.Multiplication")
"""
ch=int(input("Enter your choice:"))
if ch==1:
    c=a+b
    print("Addition is:",c)
elif ch==2:
    c=b-a
    print("Subtraction is:",c)
elif ch==3:
    c=a*b
    print("Multiplication is:",c)
else:
    print("You have entered a wrong choice.")
    
