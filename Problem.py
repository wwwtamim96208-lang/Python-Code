# Solutions to Problems 1-10

# Problem 1 
# Take two numbers as input and print their sum, subtraction,
# multiplication, and division
print("=== Problem 1 ===")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
else:
    print("Division: Cannot divide by zero")


#  Problem 2
# Determine whether a number is positive, negative, or zero
print("\n=== Problem 2 ===")
num = float(input("Enter a number: "))

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print("The number is zero")


# Problem 3 
# Print all even numbers from 1 to 100
print("\n=== Problem 3 ===")
for i in range(2, 101, 2):
    print(i, end=" ")
print()


# Problem 4 
# Take five numbers from the user and store them in a list
print("\n=== Problem 4 ===")
numbers = []
for i in range(5):
    n = float(input(f"Enter number {i + 1}: "))
    numbers.append(n)
print("Your list:", numbers)


# Problem 5
# Find the largest value in a list without using max()
print("\n=== Problem 5 ===")
largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
print("Largest value:", largest)


# Problem 6 
# Create a set from a list with duplicates and observe what happens
print("\n=== Problem 6 ===")
dup_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique_set = set(dup_list)
print("Original list:", dup_list)
print("Set:", unique_set)
print("Observation: a set keeps only unique values, so all duplicates are removed.")
print("(Sets are also unordered, so the order is not guaranteed.)")


#  Problem 7 
# Dictionary with a student's name, ID, department, and CGPA
print("\n=== Problem 7 ===")
student = {
    "name": "Rahim Uddin",
    "id": "2023-1-60-001",
    "department": "CSE",
    "cgpa": 3.75,
}
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")


# Problem 8 
# Function that returns the square of a number
print("\n=== Problem 8 ===")
def square(x):
    return x * x

n = float(input("Enter a number to square: "))
print("Square:", square(n))


# Problem 9 
# Factorial of a number using a loop
print("\n=== Problem 9 ===")
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} is {fact}")


# Problem 10 
# Count how many times each word appears in a sentence
print("\n=== Problem 10 ===")
sentence = input("Enter a sentence: ")
word_count = {}
for word in sentence.lower().split():
    word = word.strip(".,!?;:\"'")
    if word:
        word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")