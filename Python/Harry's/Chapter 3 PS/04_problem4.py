name = "Harry is a  Wizard."

print(name.find("  ")) # Double space dhundne ke liye.
print(name.find("   ")) # Triple space nai he isliye -1 ayega output me.

print(name.replace("  "," ")) 
# Double spaces ko single spaces se replace kr dega.

print(name.count("r"))

print(name) # Original String change nai hoti.
# Strings are immutable which means that you can't change them by running functions on them.
 