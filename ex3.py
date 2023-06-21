math_grades = {"John": 85, "Emily": 92, "Michael": 78, "Jessica": 95}
science_grades = {"John": 90, "Emily": 88, "Michael": 92, "Jessica": 87}

average_grades = {}

for student in math_grades:
    math_grade = math_grades[student]
    science_grade = science_grades[student]
    average_grade = (math_grade + science_grade) / 2
    average_grades[student] = average_grade

print(average_grades)
