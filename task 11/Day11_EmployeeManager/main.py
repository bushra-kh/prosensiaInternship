from manager import EmployeeManager

def menu():
    print("\nEmployee Manager")
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Search by Name/Dept")
    print("4. Sort by Salary")
    print("5. Generate Report")
    print("6. Exit")

def main():
    mgr = EmployeeManager()
    while True:
        menu()
        choice = input("Choose: ")
        if choice == "1":
            mgr.add_employee()
        elif choice == "2":
            mgr.list_employees()
        elif choice == "3":
            term = input("Search term: ")
            mgr.search_employee(term)
        elif choice == "4":
            desc = input("Sort descending? (y/n): ").lower() == "y"
            mgr.sort_by_salary(desc)
        elif choice == "5":
            mgr.generate_report()
        elif choice == "6":
            mgr.save_to_file()
            print("Saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()