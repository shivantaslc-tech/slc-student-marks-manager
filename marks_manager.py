# Student Marks Manager - Version 1
# Made by: Shivanta (SLC)

import csv

print("=== STUDENT MARKS MANAGER (SLC) ===")

# 1️⃣ Subject details
num_subjects = int(input("Enter number of subjects: "))
subjects = []

for i in range(num_subjects):
    sub = input(f"Enter name of subject {i+1}: ")
    subjects.append(sub)

students = []

# 2️⃣ Student data entry
while True:
    print("\n--- Enter Student Details ---")
    name = input("Student Name: ")
    roll = input("Roll Number: ")

    marks = []
    total = 0

    for sub in subjects:
        while True:
            try:
                m = float(input(f"Marks in {sub}: "))
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100. Try again.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        marks.append(m)
        total += m

    percentage = total / num_subjects

    student_data = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage
    }

    students.append(student_data)

    more = input("Add another student? (y/n): ").strip().lower()
    if more != 'y':
        break

# 3️⃣ Display Report
print("\n\n=== FINAL REPORT ===")
header = ["Roll", "Name"] + subjects + ["Total", "Percentage"]
print("-" * 80)
print("{:<10} {:<20}".format("Roll", "Name"), end="")

for sub in subjects:
    print("{:<10}".format(sub[:8]), end="")  # short subject name
print("{:<10} {:<10}".format("Total", "%"))
print("-" * 80)

for s in students:
    print("{:<10} {:<20}".format(s["roll"], s["name"]), end="")
    for m in s["marks"]:
        print("{:<10}".format(m), end="")
    print("{:<10} {:<10.2f}".format(s["total"], s["percentage"]))

print("-" * 80)

# 4️⃣ Save to CSV file
save = input("\nSave report to CSV file? (y/n): ").strip().lower()
if save == 'y':
    filename = "slc_marks_report.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for s in students:
            row = [s["roll"], s["name"]] + s["marks"] + [s["total"], round(s["percentage"], 2)]
            writer.writerow(row)

    print(f"Report saved as {filename}")
else:
    print("Report not saved.")

print("\nThank you for using SLC Student Marks Manager!")
