#Fibo

def  fibo(n):
    a,b,i=0,1,1
    print("Fibo is=")
    print("0\n1")
    while i<=n:
        c=a+b
        print(c)
        a,b=b,c
        i+=1

n=int(input("Enter n="))
fibo(n)






