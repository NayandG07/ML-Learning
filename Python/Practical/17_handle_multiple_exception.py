try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("Result: ", result)

except ZeroDivisionError:
    print(ZeroDivisionError)
    print("Error: Division by zero is not allowed.")

except ValueError:
    print(ValueError)
    print("Error: Invalid input. Please enter integers only.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Execution completed.")