#program to check palindrome number or not
n=int(input("Enter a number:"))
temp=n
rev=0
while n!=0:
    a=n%10
    rev=rev*10+a
    n=int(n/10)
if rev==temp:
    print("Entered number is palindrome.")
else:
    print("Entered number is not palindrome.")
