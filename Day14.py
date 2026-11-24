#Sets
numbers = {1, 2, 3, 3, 4, 4, 5}

print(numbers)

numbers.add(6)
print(numbers)

numbers.remove(2)
print(numbers)

#Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)