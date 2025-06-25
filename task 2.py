# takes a full name as input (first + last name combined)
# Slices and prints only the first name and last name using string slicing
# Then takes two numeric inputs from the user
# Performs addition, subtraction, multiplication, and division
# Displays results using formatted print() statements

fullname=input("Enter you full name: ")
pos=fullname.find(" ")
first_name=fullname[:pos]
last_name=fullname[pos+1:]
print(f'First name: {first_name}')
print(f'Last name: {last_name}')

num1=int(input("First number: "))
num2=int(input("Second number: "))

print(f"Addition: {num1+num2}")
print(f"Subtraction: {num1-num2}")
print(f"Multiplication: {num2*num1}")
print(f"Division: {num1/num2}")


