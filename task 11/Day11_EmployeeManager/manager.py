from employee import Employee
import utils

class EmployeeManager:
    def __init__(self, data_file="employee_data.txt"):
        self.data_file = data_file
        self.employees = []
        self.load_from_file()

    def load_from_file(self):
        try:
            lines = utils.read_lines(self.data_file)
            self.employees = [Employee.from_csv(line) for line in lines if line.strip()]
        except FileNotFoundError:
            self.employees = []

    def save_to_file(self):
        lines = [emp.to_csv() for emp in self.employees]
        utils.write_lines(self.data_file, lines)

    def add_employee(self):
        try:
            name = input("Name: ")
            dept = input("Department: ")
            salary = float(input("Salary: "))
            year = int(input("Joining Year: "))
            emp = Employee(name, dept, salary, year)
            self.employees.append(emp)
            print("Employee added.")
        except Exception:
            print("Invalid input. Try again.")

    def list_employees(self):
        if not self.employees:
            print("No employees found.")
        for emp in self.employees:
            emp.display()

    def search_employee(self, term):
        results = list(filter(lambda e: term.lower() in e.name.lower() or term.lower() in e.department.lower(), self.employees))
        for emp in results:
            emp.display()
        if not results:
            print("No match found.")

    def sort_by_salary(self, desc=False):
        self.employees.sort(key=lambda e: e.salary, reverse=desc)
        print("Sorted by salary.")
        self.list_employees()

    def generate_report(self, filename="employee_report.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for emp in self.employees:
                f.write(f"{emp.name} | {emp.department} | ${emp.salary:.2f} | Joined: {emp.joining_year}\n")
            f.write(f"\nTotal Employees: {len(self.employees)}\n")
        print(f"Report written to {filename}")