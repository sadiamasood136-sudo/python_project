bill = float(input("Enter total bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

if bill >= 0 and tip_percent >= 0 and people > 0:
    tip = bill * tip_percent / 100
    total_bill = bill + tip
    per_person = total_bill / people

    print("Total tip:", round(tip, 2))
    print("Total bill including tip:", round(total_bill, 2))
    print("Each person pays:", round(per_person, 2))
else:
    print("Please enter valid amounts and at least one person.")
