#WAP to calculate factorial of a number

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

n=int(input("Enter n:"))
print(fact(n))


"""
def fact (n):
    i=1
    fact1=1
    while i<=n:
        fact1=fact1*i
        i+=1
    return fact1
    n=int(input("Enter value of n:"))
factorial=fact(n)
print(factorial)
"""
