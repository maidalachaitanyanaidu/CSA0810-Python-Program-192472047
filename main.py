# 1) A shopkeeper wants to calculate the total bill for a customer. The shopkeeper has
#a list of items, where each item has a price and quantity. Write a program to
#calculate the total cost using appropriate data types
items = [
    {"price": 10.0, "quantity": 2},
    {"price": 5.5, "quantity": 4},
    {"price": 20.0, "quantity": 1}
]
total_cost = 0
for item in items:
    total_cost += item["price"] * item["quantity"]
print("Total bill: $", total_cost)
# 2)A school needs to check if a student has passed or failed based on their marks. If
#marks are greater than or equal to 50, the student passes; otherwise, they fail.
#Write a program that outputs whether the student passed or failed
marks = int(input("Enter the student's marks: "))
if marks >= 50:
    print("The student passed.")
else:
    print("The student failed.")
# 3) Write a python program to swap the value of two variables (with temporary
#variable and without temporary variable)
a = 5
b = 10
print("Before swapping (with temp): a =", a, "b =", b)
temp = a
a = b
b = temp
print("After swapping (with temp): a =", a, "b =", b)
x = 15
y = 20
print("\nBefore swapping (without temp): x =", x, "y =", y)
x, y = y, x
print("After swapping (without temp): x =", x, "y =", y)
# 4) Write a Python program to create a simple arithmetic calculator that takes two
#numbers and an operator (+, -, *, /) as input from the user and returns the result.
Use separate functions for each operation, and ensure the program handles
invalid operators and division by zero gracefully
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    result = "Error: Invalid operator!"
print("Result:", result)
# 5) Write a Python program using simple statements and expressions (exchange the
values of two variables, circulate the values of n variables and distance between
#two points)
import math
a = 5
b = 10
print("Before swapping: a =", a, "b =", b)
a, b = b, a
print("After swapping: a =", a, "b =", b)
x = 1
y = 2
z = 3
print("\nBefore circulating: x =", x, "y =", y, "z =", z)
x, y, z = z, x, y
print("After circulating: x =", x, "y =", y, "z =", z)
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("\nDistance between points:", distance)
# 6) Write a program to perform n Fibonacci series
n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
# 7) Implementing programs using Functions. (Factorial, largest number in a list and
#area of shape)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = 5
print("Factorial of", num, "is", factorial(num))
# 8) Solve the Scientific problems using Conditionals and Iterative loops. (Number
#series, Number Patterns and pyramid pattern)
# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, ...
def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
fibonacci_series(10)
# Pattern: 
# 1
# 1 2
# 1 2 3
# ...
def number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage
number_pattern(5)
# Pyramid Pattern:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)
# 9)  Write a program to find the LCM and GCD of a given number.
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return (a * b) // gcd
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = find_gcd(num1, num2)
lcm = find_lcm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
print("LCM of", num1, "and", num2, "is:", lcm)
# 10)  Implementing programs using Strings. (reverse, character count and replacing
#characters)
def reverse_string(s):
    return s[::-1]
string = input("Enter a string: ")
# Reversing the string
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)


