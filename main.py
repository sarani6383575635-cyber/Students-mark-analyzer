import csv
import os

name = input("Enter student full name: ")

Subjects = ["Python", "Database", "Maths", "Java", "DS"]
marks = []

for Subject in Subjects:
    mark = float(input(f"Enter marks for {Subject}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "B+"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

result = "Pass" if average >= 40 else "Fail"


cgpa = average / 10

print("\nStudent name:", name)
print("Total marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("CGPA:", round(cgpa, 2))
print("Result:", result)

# Save result in CSV file
file_name = "Student_results.csv"
file_exists = os.path.exists(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student Name",
            "Total Marks",
            "Average",
            "Grade",
            "CGPA",
            "Result"
        ])

    writer.writerow([
        name,
        total,
        round(average, 2),
        grade,
        round(cgpa, 2),
        result
    ])

print("\nResult has been saved to Student_results.csv")