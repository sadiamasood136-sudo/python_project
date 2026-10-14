students = {
    "Ali": 85,
    "Ayesha": 92,
    "Ahmed": 76,
    "Fatima": 65,
    "Usman": 58
}

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"

    print(name, "- Marks:", marks, "- Grade:", grade)
