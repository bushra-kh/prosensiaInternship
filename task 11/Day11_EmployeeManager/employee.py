class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.joining_year = int(joining_year)

    def display(self):
        print(f"{self.name} | {self.department} | ${self.salary:.2f} | Joined: {self.joining_year}")

    def to_csv(self):
        return f"{self.name},{self.department},{self.salary},{self.joining_year}"

    @staticmethod
    def from_csv(line):
        name, department, salary, joining_year = line.strip().split(",")
        return Employee(name, department, float(salary), int(joining_year))