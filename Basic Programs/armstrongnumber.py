#program to check armstrong number or not
n=int(input("Enter a number:"))
temp=n
sum=0
while n!=0:
    a=n%10
    sum=sum+a*a*a
    n=int(n/10)
if sum==temp:
    print("Entered number is armstrong.")
else:
    print("Entered number is not armstrong.")
