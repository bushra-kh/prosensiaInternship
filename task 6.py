# Conditional Grading System Using if/elif/else

def evaluate_grade(score: float) -> str:
# 90–100: A, 85–89: A-, 80–84: B+, 75–79: B, 70–74: B-,
# 65–69: C+, 60–64: C, 50–59: D, <50: F
    if 90<=score<=100:
        grade='A'
    elif 85<=score<=89:
        grade='A-'
    elif 80<=score<=84:
        grade='B+'
    elif 75<=score<=79:
        grade='B'
    elif 70<=score<=74:
        grade='B-'
    elif 65<=score<=69:
        grade='C+'
    elif 60<=score<=64:
        grade='C'
    elif 50<=score<=59:
        grade='D'
    elif score<50:
        grade='F'
    else:
        print('Invalid score!')

    return grade

def print_grade_summary(student_name: str = 'Unnamed', score: float = 0.0):
    print(f'Student {student_name} scored {score} → Grade: {evaluate_grade(score)}')

print_grade_summary(student_name='Zara', score=87.5)