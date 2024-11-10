class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        old_salary = self.salary
        self.salary = new_salary
        print(f"Updated salary for {self.name} from ${old_salary:.2f} to ${self.salary:.2f}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} (ID: {employee.employee_id}) to the {self.department_name} department.")

    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name} department: ${total_salary:.2f}")
        return total_salary

    def display_all_employees(self):
        if self.employees:
            print(f"\nEmployees in the {self.department_name} department:")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in the {self.department_name} department.")

# Interactive code to manage department and employees

# Sample department
department = Department("Finance")

# Menu for interaction
def department_menu():
    while True:
        print("\nDepartment Menu:")
        print("1. Add an Employee")
        print("2. Update an Employee's Salary")
        print("3. Display All Employees")
        print("4. Calculate Total Salary Expenditure")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = input("Enter employee salary: ")

            try:
                salary = float(salary)
                employee = Employee(name, employee_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid salary format. Please enter a numeric value.")

        elif choice == '2':
            employee_id = input("Enter employee ID to update salary: ")
            employee = next((emp for emp in department.employees if emp.employee_id == employee_id), None)

            if employee:
                new_salary = input("Enter new salary: ")
                try:
                    new_salary = float(new_salary)
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Invalid salary format. Please enter a numeric value.")
            else:
                print("No employee found with that ID.")

        elif choice == '3':
            department.display_all_employees()

        elif choice == '4':
            department.calculate_total_salary_expenditure()

        elif choice == '5':
            print("Exiting the department menu.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the interactive menu
department_menu()
