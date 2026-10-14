full_name = input("Enter your full name: ").strip()

space_position = full_name.find(" ")

if space_position != -1:
    first_name = full_name[:space_position]
    last_name = full_name[space_position + 1:].strip()

    print("First name:", first_name)
    print("Last name:", last_name)
    print("Initials:", first_name[0].upper() + ". " + last_name[0].upper() + ".")
    print("Uppercase name:", full_name.upper())
    print("Reversed name:", full_name[::-1])
else:
    print("Please enter both first and last name.")
