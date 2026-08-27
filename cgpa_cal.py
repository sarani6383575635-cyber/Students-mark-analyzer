name = input ("enter student name:")
num_subjects = int (input("enter number of subjects:"))
total_grade_points = 0
for i in range(num_subjects):
    grade_point = float(input(f"enter grade point for subjects {i+1}:v "))
    total_grade_points += grade_point
cgpa = total_grade_points / num_subjects
print ("\n---STUDENT RESULT---")
print("student name:",name)
print("CGPA:",round(cgpa,2))