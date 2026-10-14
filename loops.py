
# For loop
for i in range(1, 6):
    print(i)

# While loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Break statement
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# Continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# For loop with else
for i in range(1, 4):
    print("Number:", i)
else:
    print("Loop completed")

# While loop with else
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("While loop completed")
