try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    result = numerator / denominator
    print("Result: ", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    print(ZeroDivisionError)

except ValueError:
    print("Error: Please enter valid integers.")
    print(ValueError)

finally:
    print("Execution completed.")