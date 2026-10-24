# a = (1,) # Tuple with ONLY ONE element requires a comma.

a = (1,45,342,3424,False,45, "Rohan", "Shivam")
print(a)

# a.count(45) # No. of times "45" occurs in 'a'.
no = a.count(45) # Same as above.
print(no)

i = a.index(45) # Retruns the INDEX of the ELEMENT. But ek baar mil jaye toh ye aage check nai karega for repeating occurances.
j = a.index(3424) # Simplified = Returns the FIRST INDEX of the Element.

print(i)
print(j)

print(a[0])
print(a[1:]) 

# CONCATENATION of Tuples
a1 = (1,2)
a2 = (3,4)

print(a1 + a2)

# REPETITION
a_repeated = a1 * 3 #
print(a_repeated)

# Checking if an ELEMENT is Present in a tuple or not.

exists_1 = 2 in a
exists_2 = 2 in a1
print(exists_1)
print(exists_2)

print(len(a))

# Iterate through a Tuple
for item in a:
    print(item)

# Unpacking Tuple elements into VARIABLES.
x, y = a1
print(x)
print(y)
