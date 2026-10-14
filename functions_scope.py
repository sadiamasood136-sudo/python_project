
# Simple function
def greet():
    print("Hello, welcome to Python")

greet()

# Function with parameters
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# Local variable
def show_message():
    message = "This is a local variable"
    print(message)

show_message()

# Global variable
name = "Sadia"

def display_name():
    print(name)

display_name()

# Modifying a global variable
counter = 0

def update_counter():
    global counter
    counter = counter + 1

update_counter()
print("Counter:", counter)
