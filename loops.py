# Loops
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# For else statement
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    # This will be executed if the loop completes without finding a successful attempt
    print("Attempted 3 times and failed")

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# iterables
print(type(5))  # <class 'int'>
print(type(range(5)))  # <class 'range'>

for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break


sum = 0
for number in range(2, 10, 2):
    print(number)
    sum += 1
print(f"We have {sum} even numbers")

# or
sum = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        sum += 1
print(f"We have {sum} even numbers")
