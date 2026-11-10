# Conditional Statements
temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

if not student:
    print("Eligible for loan")
else:
    print("Not Eligible for loan")

if (high_income or good_credit) and not student:
    print("Eligible for loan")

# In python logical operators are short circuit operators.
# In AND: when the first condition is false, it will not check the second condition.
# In OR: when the first condition is true, it will not check the second condition.

# chaining comparison operators
age = 22
if 18 <= age < 65:
    print("Eligible")

# Quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
