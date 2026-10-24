user_input = input("Enter Something: ")

try:
    evaluated_input = eval(user_input)
    print("You entered: ", evaluated_input)
    print("Data Type of the input is: ", type(evaluated_input))
except:
    print("Invalid Input")