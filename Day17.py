#List comprehention
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)

#List comprehention with condition
numbers = range(1, 11)

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)