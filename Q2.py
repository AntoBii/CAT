class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        if self.assignments:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f" - {assignment}: {grade}")
        else:
            print(f"No grades recorded for {self.name}.")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"No student found with ID {student_id}.")

    def display_all_students_and_grades(self):
        if self.students:
            print(f"\nAll students and their grades in '{self.course_name}':")
            for student in self.students:
                print(f"\nStudent: {student.name} (ID: {student.student_id})")
                student.display_grades()
        else:
            print("No students enrolled in this course.")

# Interactive code for adding students and assigning grades

# Sample instructor
instructor = Instructor("Dr. Smith", "Computer Science 101")

# Menu for instructor interactions
def instructor_menu():
    while True:
        print("\nInstructor Menu:")
        print("1. Add a Student")
        print("2. Assign Grade to Student")
        print("3. Display All Students and Grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            student = Student(name, student_id)
            instructor.add_student(student)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            grade = input("Enter grade: ")
            try:
                grade = float(grade)  # Convert to float for numerical grade values
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid grade format. Please enter a numeric value.")

        elif choice == '3':
            instructor.display_all_students_and_grades()

        elif choice == '4':
            print("Exiting the instructor menu.")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the interactive menu
instructor_menu()
