a = int(input("Enter your age: "))

# if statement no.1
if(a%2==0):
    print("a is even")

# End

# if statement no.2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Invalid input!")

else:
    print("You are below the age of consent")

# End

print("End of program")