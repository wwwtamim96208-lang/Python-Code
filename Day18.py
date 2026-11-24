#Useful built in Function
numbers = [5, 2, 9, 1, 7]

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))

#Exception handling
try:
    number = int(input("Enter an integer: "))
    result = 10 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

#impoting modules
import math
print(math.sqrt(25))
print(math.pow(2, 3))
print(math.pi)