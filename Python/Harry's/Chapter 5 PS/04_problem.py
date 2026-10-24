s = set()
s.add(20)
s.add(20.0)
s.add('20') # This will be added to the set as a string, not as an integer or float.

print(s)
# 1 == 1.0 as long as the values are equal, Python ignores the data type.