print("="*40)
print("PERSONAL POCKET CGPA CALCULATOR (PPC)")
print("="*40)
print()

num_courses = int(input("How many courses are you offering? "))
print()

total_credit_units = 0
total_grade_points  = 0

count = 1
while count <= num_courses:
    print("- Course", count,)
    course_name  = input("Course code/name: ")
    credit_unit  = int(input("Credit unit: "))
    grade_letter = input("Grade (A/B/C/D/E/F): ").upper()

    if grade_letter == "A":
        grade_point = 5
    elif grade_letter == "B":
        grade_point = 4
    elif grade_letter == "C":
        grade_point = 3
    elif grade_letter == "D":
        grade_point = 2
    elif grade_letter == "E":
        grade_point = 1
    elif grade_letter == "F":
        grade_point = 0
    else:
        print("The Only Acceptable Grade Letters Are A-F")
        continue

    quality_point = credit_unit * grade_point

    total_credit_units = total_credit_units + credit_unit
    total_grade_points  = total_grade_points  + quality_point

    print("Quality Point:", quality_point)
    print()
    count = count + 1

if total_credit_units == 0:
    print("Your Credit Units Cannot Be Zero (0). Please Cross-Check, Then Try Again!")
else:
    cgpa = total_grade_points / total_credit_units

    if cgpa >= 4.50:
        grade_class = "First Class"
    elif cgpa >= 3.50:
        grade_class = "Second Class Upper"
    elif cgpa >= 2.40:
        grade_class = "Second Class Lower"
    elif cgpa >= 1.50:
        grade_class = "Third Class"
    else:
        grade_class = "Pass"

    print("="*40)
    print("         CGPA RESULT SUMMARY         ")
    print("="*40)
    print("Total Credit Units :", total_credit_units)
    print("Total Grade Points :", total_grade_points)
    print("Your CGPA          :", round(cgpa, 2))
    print("Class of Degree    :", grade_class)
    print("="*40)