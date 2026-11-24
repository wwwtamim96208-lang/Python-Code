#forloops
for i in range(5):
    print(i)

#using range(start,stop,step)
for i in range(1, 11, 2):
    print(i)

#Loop through string
for character in "Python":
    print(character)

#While Loop
count = 1
while count <= 5:
    print(count)
    count += 1

    #Break and Continue
    print("Using break:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\nUsing continue:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
