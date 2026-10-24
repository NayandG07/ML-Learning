# Open a file in write mode
with open("output.txt", "w") as file:
    # Write data to the file
    file.write("Hello, this is a sample text.\n")
    file.write("This is the second line of the text.\n")

print("Data has been written to output.txt")

with open("output.txt", "r") as file:
    # Read the data from the file
    content = file.read()
    print("Content of the file:")
    print(content)
