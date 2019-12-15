def palindrome():
    myString="Devvrat"
    myString=myString.lower()
    revString=reversed(myString)
    if list(myString) == list(revString):
        print("String is Pallindrome")
    else:
        print("String is not Pallindrome")

    
