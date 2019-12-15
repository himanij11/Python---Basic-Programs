#menu driven for even,palindrome,armstrong

def even(n):
    if(n%2==0):
        print("{} is an even number.".format(n))
    else:
        print("{} is not an even no.".format(n))

def palindrome(n):
    temp=n
    rev=0
    while n!=0:
        a=n%10
        rev=rev*10+a
        n=int(n/10)
    if  temp==rev:
        print("{} is a palindrome number.".format(temp))
    else:
         print("{} is not a palindrome number.".format(temp))

def armstrong(n):
    temp=n
    sum=0
    while n!=0:
        a=n%10
        sum=sum+a*a*a
        n=int(n/10)
    if temp==sum:
         print("{} is a armstrong number.".format(temp))
    else:
         print("{} is not an armstrong number.".format(temp))

n=int(input("enter n:"))
ch=int(input("1.Even no \n2.Palindrome \n3.Armstrong \n4.Exit \nEnter choice="))
while ch!=4:
    if ch==1:
        even(n)
    elif ch==2:
        palindrome(n)
    else:
        armstrong(n)
    n=int(input("enter n:"))
    ch=int(input("1.Even no \n2.Palindrome \n3.Armstrong \n4.Exit \nEnter choice="))
