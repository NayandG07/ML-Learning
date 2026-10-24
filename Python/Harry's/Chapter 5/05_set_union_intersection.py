s1 = {1, 45, 6, 78}
s2 = {7, 8, 1, 78}

print(s1.union(s2)) # {1, 45, 6, 7, 8, 78}

print(s1.intersection(s2)) # {1, 78}
print(s1.difference(s2)) # {45, 6}
print(s1-s2) # {45, 6}

print({1, 6}.issubset(s1)) # True
print(s1.issuperset({1, 6})) # True