#Lists
numbers = [10, 20, 30, 40]

print(numbers)
print(numbers[0])
print(numbers[-1])

numbers.append(50)
print(numbers)

numbers.remove(20)
print(numbers)

numbers[0] = 100
print(numbers)

print("Length:", len(numbers))

#Loop through a List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)