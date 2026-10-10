from student import Student
from student_manager import StudentManager
from storage import load_students, save_students
manager = StudentManager()
# Load students from students.json
manager.students = load_students("students.json", Student)
while True:
 print("\n===== Student Management System =====")
 print("1. Add Student")
 print("2. View Students")
 print("3. Find Student")
 print("4. Update Student")
 print("5. Delete Student")
 print("6. Exit")
 choice = input("Enter your choice: ")
 if choice == "1":
 # Read student details
 name = input("Enter student name: ")
 age = int(input("Enter student age: "))
 python = float(input("Enter Python marks: "))
 mathematics = float(input("Enter Mathematics marks: "))
 communication = float(input("Enter Communication marks: "))
 # Create a Student object
 student = Student(
 name,
 age,
 python,
 mathematics,
 communication
 )
 # Add the student to the manager
 manager.add_student(student)
 # Save students
 save_students(manager.students, "students.json")
    print("Student added successfully.")
 elif choice == "2":
 # View students
 manager.view_students()
 elif choice == "3":
 # Read a name
 name = input("Enter student name: ")
 # Find the student
 student = manager.find_student(name)
 # Display the student if found
 if student:
 student.display()
 else:
 print("Student not found.")
 elif choice == "4":
 # Read the student name and new marks
 name = input("Enter student name: ")
 python = float(input("Enter new Python marks: "))
 mathematics = float(input("Enter new Mathematics marks: "))
 communication = float(input("Enter new Communication marks: "))
 # Update the student
 if manager.update_student(
 name,
 python,
 mathematics,
 communication
 ):
 # Save students
 save_students(manager.students, "students.json")
 print("Student updated successfully.")
 else:
 print("Student not found.")
 elif choice == "5":
 # Read the student name
 name = input("Enter student name: ")
 # Delete the student
 if manager.delete_student(name):
 # Save students
 save_students(manager.students, "students.json")
 print("Student deleted successfully.")
 else:
 print("Student not found.")
 elif choice == "6":
 print("Exiting application.")
 break
 else:
 print("Invalid choice.")
2. storage.py
import json
def save_students(students, filename):
 """Save students to a JSON file."""

 # Convert students into dictionaries
 data = []
 for student in students:
 data.append({
 "name": student.name,
 "age": student.age,
 "python": student.python,
 "mathematics": student.mathematics,
 "communication": student.communication
 })
 # Save the data using json.dump()
 with open(filename, "w") as file:
 json.dump(data, file, indent=4)
def load_students(filename, student_class):
 """Load students from a JSON file."""

 try:
 # Open and read the JSON file
 with open(filename, "r") as file:
 data = json.load(file)
 # Convert dictionaries back into Student objects
 students = []
 for student_data in data:
 student = student_class(
 student_data["name"],
 student_data["age"],
 student_data["python"],
 student_data["mathematics"],
 student_data["communication"]
 )
 students.append(student)
 return students
 except FileNotFoundError:
 return []
 except json.JSONDecodeError:
 print("Error: Invalid JSON file.")
 return []
3. student.py
class Student:
 """Represent a student."""
 def __init__(self, name, age, python, mathematics, communication):
 # Store the student details
 self.name = name
 self.age = age
 self.python = python
 self.mathematics = mathematics
 self.communication = communication
 def calculate_percentage(self):
 """Calculate the student's percentage."""

 total = self.python + self.mathematics + self.communication
 percentage = total / 3

 return percentage
 def display(self):
 """Display the student's details."""

 print(f"Name: {self.name}")
 print(f"Age: {self.age}")
 print(f"Python: {self.python}")
 print(f"Mathematics: {self.mathematics}")
 print(f"Communication: {self.communication}")
 print(f"Percentage: {self.calculate_percentage():.2f}%")
4. student_manager.py
class StudentManager:
 """Manage a collection of students."""
 def __init__(self):
 # Create a collection to store students
 self.students = []
 def add_student(self, student):
 """Add a student to the collection."""

 self.students.append(student)
 def view_students(self):
 """Display all students."""

 if not self.students:
 print("No students found.")
 return
 for student in self.students:
 student.display()
 print("--------------------")
 def find_student(self, name):
 """Find a student by name."""

 for student in self.students:
 if student.name.lower() == name.lower():
 return student
 return None
 def update_student(self, name, python, mathematics, communication):
 """Update marks for an existing student."""

 student = self.find_student(name)
 if student:
 student.python = python
 student.mathematics = mathematics
 student.communication = communication
 return True
 return False
 def delete_student(self, name):
 """Delete a student by name."""

 student = self.find_student(name)
 if student:
 self.students.remove(student)
 return True
 return False
FOLDER –FUNCTIONS
1. student_functions.py
# Day 1 - Python Fundamentals
student_name = input("Enter student name:")
marks_python = float(input("Enter marks for Python:"))
marks_math = float(input("Enter marks for Mathematics:"))
marks_comm = float(input("Enter marks for Communication:")
# Create a function to calculate the percentage
def calculate_percentage(python, mathematics, communication):
 total = python + mathematics + communication
 percentage = total / 3
 return percentage
percentage = calculate_percentage(
 marks_python,
 marks_math,
 marks_comm
)
print("\n -- Result --")
print("Student:", student_name)
print("Percentage:", percentage)
FOLDER – MODULES
1.results_calculator.py
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))
def calculate_percentage(mark1, mark2, mark3):
 total = mark1 + mark2 + mark3
 percentage = total / 3
 return percentage
percentage = calculate_percentage(mark1, mark2, mark3)
print("This is the percentage:", percentage)
2.students_module.py
from modules.result_calculator import calculate_percentage
student_name = input("Enter student name: ")
marks_python = float(input("Enter Python marks: "))
marks_math = float(input("Enter Mathematics marks: "))
marks_comm = float(input("Enter Communication marks: "))
percentage = calculate_percentage(
 marks_python,
 marks_math,
 marks_comm
)
print("\n--- Result ---")
print(f"Student: {student_name}")
print(f"Percentage: {percentage}")
