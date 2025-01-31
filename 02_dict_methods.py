marks = {
    "Harry": 100,
    "Hermione": 56,
    "Ron": 34,
    0: "Jhon"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99})
# print(marks)

print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error