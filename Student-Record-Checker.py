# Code with the help of AI
# Day 10:

students = {
    "Farah": 95,
    "Arham": 86,
    "Hammad": 90,
    "Hashir": 82,
    "Maham": 89
}

while True:  # for infinite loop
    name = input("Enter student name (or type 'exit' to quit): ")
    
    if name.lower() == "exit":
        print("Goodbye!")
        break

    if name in students:
        marks = students[name]
        print(f"{name}'s marks: {marks}")
        
        # Determine the grade based on marks
        if marks >= 90:
            print("Grade: A+")
        elif marks >= 80:
            print("Grade: A")
        elif marks >= 70:
            print("Grade: B")
        else:
            print("Grade: C or below")
    else:
        print("Student not found!")

# Optional: Print all students and their marks
print(students)
