#aliasing

# Original list
original_list = [1, 2, 3, 4, 5]

# Aliasing the original list
alias_list = original_list

# Modifying the alias list
alias_list.append(6)

# Printing both lists to show that they both reflect the change
print("Original List:", original_list)
print("Alias List:", alias_list)

#so to copy value use a = b[:]

# Demonstrating the difference between append and extend

# Using append
list_append = [1, 2, 3]
list_append.append([4, 5])
print("List after append:", list_append)  # Output: [1, 2, 3, [4, 5]]

# Using extend
list_extend = [1, 2, 3]
list_extend.extend([4, 5])
print("List after extend:", list_extend)  # Output: [1, 2, 3, 4, 5]

#append can only add one element (so add a number of elements as a list) at a time while extend can add multiple elements by iterating over them.

# Checking if a number is 0, positive, or negative without using elif

# Input number
num = float(input("Enter a number: "))

# Using if-else to determine the nature of the number
if num > 0:
    print("The number is positive.")
else:
    if num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")



# Generating a dictionary of students with their grades
students_grades = {
    "Alice": [85],
    "Bob": [92],
    "Charlie": [78],
    "David": [90],
    "Eva": [88]
}

# Function to add a new student
def add_student(students_grades, new_student):
    if new_student not in students_grades:
        students_grades[new_student] = []
    else:
        print(f"Student {new_student} already exists.")

# Function to print all grades of a student
def print_grades(students_grades, student_name):
    if student_name in students_grades:
        print(f"Grades for {student_name}: {students_grades[student_name]}")
    else:
        print(f"Student {student_name} not found.")

# Function to add grades for a student
def add_grades(students_grades, student_name, new_grades):
    if student_name in students_grades:
        students_grades[student_name].extend(new_grades)
    else:
        print(f"Student {student_name} not found.")

# Example usage
add_student(students_grades, "Frank")
add_grades(students_grades, "Frank", [75, 80, 85])
add_grades(students_grades, "Frank", [92])
print_grades(students_grades, "Frank")
print_grades(students_grades, "Bob")
print(students_grades)


# Demonstrating the difference between local and global variables

# Global variable
global_var = "I am a global variable"

def my_function():
    # Local variable
    local_var = "I am a local variable"
        
    # Accessing the global variable inside the function
    print(global_var)
        
    # Accessing the local variable inside the function
    print(local_var)

# Calling the function
my_function()

# Accessing the global variable outside the function
print(global_var)

# Trying to access the local variable outside the function will raise an error
try:
    print(local_var)
except NameError as e:
    print(e)

class StudentGrades:
    def __init__(self):
        self.students_grades = {
                "Alice": [85],
                "Bob": [92],
                "Charlie": [78],
                "David": [90],
                "Eva": [88]
        }

    def add_student(self, new_student):
        if new_student not in self.students_grades:
            self.students_grades[new_student] = []
        else:
            print(f"Student {new_student} already exists.")

    def print_grades(self, student_name):
        if student_name in self.students_grades:
            print(f"Grades for {student_name}: {self.students_grades[student_name]}")
        else:
            print(f"Student {student_name} not found.")

    def add_grades(self, student_name, new_grades):
        if student_name in self.students_grades:
            self.students_grades[student_name].extend(new_grades)
        else:
            print(f"Student {student_name} not found.")

# Example usage
student_grades = StudentGrades()
student_grades.add_student("Frank")
student_grades.add_grades("Frank", [75, 80, 85])
student_grades.add_grades("Frank", [92])
student_grades.print_grades("Frank")
student_grades.print_grades("Bob")
print(student_grades.students_grades)