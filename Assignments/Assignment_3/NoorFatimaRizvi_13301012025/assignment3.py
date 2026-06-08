#Assignment 3
# Q1.
def print_natural_numbers():
    for i in range(1, 11):
        print(i)

print_natural_numbers()

# Q2.
def sum_natural_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print("Sum =", total)

sum_natural_numbers(10)

# Q3.
def reverse_number(n):
    reversed_num = int(str(n)[::-1])
    print("Reversed =", reversed_num)

reverse_number(9876)

# Q4.
def count_digits(n):
    count = len(str(n))
    print("Number of digits =", count)

count_digits(8967)

# Q5.
def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        print(n, "is a palindrome")
    else:
        print(n, "is not a palindrome")

check_palindrome(292)
check_palindrome(298)

# Q6.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(11)

# Q7.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Select operation: 1-Add  2-Subtract  3-Multiply  4-Divide")
choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result =", add(num1, num2))
elif choice == '2':
    print("Result =", subtract(num1, num2))
elif choice == '3':
    print("Result =", multiply(num1, num2))
elif choice == '4':
    print("Result =", divide(num1, num2))
else:
    print("Invalid choice")

# Q8.
student_name = input("Enter student name: ")
student_marks = input("Enter student marks: ")

with open("students.txt", "w") as student_file:
    student_file.write("Name: " + student_name + "\n")
    student_file.write("Marks: " + student_marks + "\n")

print("Student details saved successfully!")

# Q9.
with open("students.txt", "r") as student_file:
    student_data = student_file.read()

print("Student Details:")
print(student_data)

# Q10.
try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    division_result = first_number / second_number
    print("Division Result:", division_result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Q11.
class Student:
    def __init__(self, student_name, student_marks):
        self.student_name = student_name
        self.student_marks = student_marks

    def display_details(self):
        print("Student Name:", self.student_name)
        print("Student Marks:", self.student_marks)

student_name = input("Enter student name: ")
student_marks = int(input("Enter student marks: "))

student_object = Student(student_name, student_marks)
student_object.display_details()