username = input("Enter username: ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
elif(len(username)>10):
    print("Your username contains more than 10 characters")
else:
    print("Your username contains 10 characters")