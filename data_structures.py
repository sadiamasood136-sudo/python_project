
# List: can be changed
fruits = ["apple", "banana", "mango"]
print(fruits)

fruits.append("orange")
print(fruits)

print(fruits[0])
fruits[1] = "grapes"
print(fruits)

# Tuple: cannot be changed
colors = ("red", "green", "blue")
print(colors)
print(colors[1])

# Set: stores unique values
numbers = {1, 2, 2, 3, 4}
print(numbers)

numbers.add(5)
print(numbers)
numbers.remove(2)
print(numbers)

# Dictionary: key-value pairs
student = {
    "name": "Sadia",
    "age": 20,
    "marks": 85
}

print(student)
print(student["name"])

student["age"] = 21
student["city"] = "Pakistan"
print(student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
