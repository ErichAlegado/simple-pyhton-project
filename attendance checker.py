# Simple Attendance Checker

# List of students (you can change/add names)
students = ["Alice", "Lian", "Ellana", "Cj", "Akiennah"]

# Dictionary to store attendance
attendance = {}

print("=== Attendance Checker ===\n")

# Loop through each student to mark attendance
for student in students:
    while True:
        status = input(f"Is {student} present? (y/n): ").strip().lower()
        if status == "y":
            attendance[student] = "Present"
            break
        elif status == "n":
            attendance[student] = "Absent"
            break
        else:
            print("Invalid input! Please type 'y' or 'n'.")

# Display the attendance report
print("\n=== Attendance Report ===")
for student, status in attendance.items():
    print(f"{student}: {status}")
