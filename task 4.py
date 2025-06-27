# Student Record System with Tuples & Sets
# Stores immutable student IDs using a tuple
# Creates a set of unique course names (e.g., Python, AI, ML)
# Adds, removes, and prints course names dynamically
# Uses inline comments to describe each logic block

std=('cs009', 'cs006', 'ai89', 'ds19', 'ds01')  # tuple of student IDs of string datatype
print(f'Student IDs: {std}')                    # print IDs

courses={'Python', 'AI', 'ML', 'C++', 'Calculus'}   # set of courses
print(f'Courses originally: {courses}')

courses.add(input("Add another course: "))          # appending a course through add method
print(f'Courses: {courses}')

courses.remove(input("Remove an existing course: ")) # removing a course through remove method
print(f'Courses: {courses}')

courses.discard(input("Remove an existing course: ")) # removing a course through discard method
print(f'Courses: {courses}')                          # print final courses set




