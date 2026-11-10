# Numbers
import math


x = 1
x = 1.1
x = 1 + 2j  # complex number: a + bi

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # float division
print(10 // 3)  # integer division
print(10 % 3)  # remainder
print(10 ** 3)  # exponentiation

x = 10
x += 3

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))  # rounds up to the nearest integer
print(math.floor(2.2))  # rounds down to the nearest integer

x = input("x: ")
print(type(x))
y = int(x) + 1
print(f"x: {x}, y: {y}")

int(x)
float(x)
bool(x)
str(x)

# Falsy values: 0, 0.0, "", None
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(1))  # True
print(bool(-1))  # True
print(bool(""))  # False
print(bool("False"))  # True
