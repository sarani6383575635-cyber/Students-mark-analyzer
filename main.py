import csv
import os

name = input("enter student full name:")
Subjects = ["python","database","maths","java","DS"]
marks = []
for Subject in Subjects:
    mark = float (input(f"enter marks for {Subjects}:"))
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
result ="pass" if average >= 40 else "fail"
print(f"Student name: {name}")
print(f"Total marks: {total}")
print(f"average: {average:.2f}")
print(f"grade: {grade}")
print(f"result: {result}")

file_name = "Student_results.csv"
file_exists = os.path.exists(file_name)
with open(file_name,"a",newline = "") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow([
            "Student name",
            "Total marks",
            "average",
            "grade",
            "results"
        ])

    writer.writerow([
        name,
        total,
        round(average,2),
        grade,
        result
    ])    
print("\nResult has been saved to Student_results.csv")
