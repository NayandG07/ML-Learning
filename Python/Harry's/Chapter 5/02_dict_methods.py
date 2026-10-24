marks = {
    "Harry": 100,
    "Ron": 80,
    "Hermione": 95
}

print(marks.items())
print(marks.keys())
print(marks.values())
print(len(marks)) # Length: 3

marks.update({"Harry": 99})
print(marks)

print(marks.get("Harry"))
# print(marks.get("Snape")) # Return: None

# print(marks.get("Harry2")) # Prints: None
# print(marks["Harry2"]) # Raises KeyError

print("New Dictionary")
marks_1 = {
    "Harry": 100,
    "Ron": 80,
    "Hermione": 95
}
print(marks_1.pop("Ron")) # Returns: 80
print(marks_1) # {'Harry': 100, 'Hermione': 95}
print(marks_1.popitem()) # Returns the last item in the dictionary i.e. ('Hermione', 95)
print(marks_1) 