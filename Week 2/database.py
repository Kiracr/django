
student_database = {}
   

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student_database[name] = {
        'age': age,
        'grade': grade
    }
    print(student_database[name])
    print(student_database)
    print("Student added successfully!")
def view_student():
    name = input("Enter student name: ")
    if name in student_database:
        student = student_database[name]
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        # Print other relevant details here
    else:
        print("Student not found!")

# Function to list all students in the database
def list_students():
    if not student_database:
        print("No students in the database.")
    else:
        for name, student in student_database.items():
            print("Name:", name)
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            print() 
        print("Total students:", len(student_database))


def update_student():
    name = input("Enter student name: ")
    if name in student_database:
        student = student_database[name]
        print("Current information for", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        new_age = input("Enter new age (press Enter to skip): ")
        if new_age:
            student['age'] = new_age
        
        new_grade = input("Enter new grade (press Enter to skip): ")
        if new_grade:
            student['grade'] = new_grade

        print("Student information updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    name = input("Enter student name: ")
    if name in student_database:
        del student_database[name]
        print("Student deleted successfully!")
    else:
        print("Student not found!")


while True:
    print("Student Database")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

        
  