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
