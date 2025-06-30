gmapping = {
    'A+': 4.0, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'F': 0.0}

def print_gpa_summary(student_name: str, gpa: float):
    print(f"Student {student_name}'s GPA: {round(gpa, 2)}")

def calculate_weighted_gpa(grades: list[tuple[str, float]]) -> float:
    total_points=total_credits=0.0
    
    for grade, credit in grades:
        grade_point = gmapping.get(grade.upper(), 0.0)
        total_points += grade_point * credit
        total_credits += credit
    if total_credits == 0:
        return 0.0
    return total_points / total_credits

grades_list = [('A', 3), ('B+', 4), ('C', 2)]
student = "ali"
gpa = calculate_weighted_gpa(grades_list)
print_gpa_summary(student_name=student, gpa=gpa)