#Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z, end="\n\n")

x = "Nazia mam "
y = "is "
z = "Best"
print(x + y + z )

x = "Art of living "
y = "is "
z = "the best course"
print(x ,y , z,end ="\n\n")

x = 5
y = 17
z = 19
print(x + y + z,end ="\n\n")

#Global variables

x = "Beautiful"

def myfunc():
  x = "fantastic"
  print("Nazia mam is " + x)

myfunc()

print("Nazia mam is " + x)

