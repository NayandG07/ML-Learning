# Initialize variables
sum_even = 0
num = 1

# Calculate sum of even numbers from 1 to 100
while num <= 100:
    if num % 2 == 0:  # Check if even
        sum_even += num
    num += 1

# Display result
print(f"Sum of even numbers from 1 to 100: {sum_even}") 