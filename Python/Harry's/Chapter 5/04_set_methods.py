s = {1, 5, 32, 54, 5, 5, 5, "Harry"}

print(s, type(s))

s.add(566) # Add an element to the set
print(s, type(s))
s.remove(1) # Remove 1 from set s
print(s, type(s))
print(s.pop()) # Remove a random element and returns it. 
print(s)

s1 = {1, 5, 32, 54, 5, 5, 5, "Harry"}
set.clear(s1) # Clear all elements from set s1
print(s1)