# Functions
def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}! Welcome to the program.")


# It is a good practise to have two blank lines after a function definition.
greet("Mosh", "Hamedani")
# returns None because the function does not return anything
print(greet("Mosh", "Hamedani"))


def get_greeting(name):
    return f"Hi {name}!"


message = get_greeting("Mosh")

# def increment(number, by=1, another): wrong because default parameters should be at the end of the parameter list
# def increment(number, another, by=1):


def increment(number, by=1):
    return number + by


print(increment(2, by=1))
print(increment(2))  # by=1 is the default value


def multiply(*numbers):
    print(numbers)  # prints a tuple of all the numbers passed as arguments
    # (2, 3, 4, 5)
    total = 1
    for number in numbers:
        print(number)  # prints each number in the tuple
        total *= number
    return total


print(multiply(2, 3, 4, 5))
