# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])  # started from end
print(course[0:3])  # last index 3 is not included
print(course[0:])  # starts from 0 index and goes till end
print(course[:3])  # by default starts from 0 till 2nd index
print(course[:])  # copy of the string value

course = "Python \"Programming"
print(course)
course = "Python \'Programming"
course = "Python \\Programming"
course = "Python \nProgramming"  # new line

first = "Mosh"
last = "Hamedani"
full = first + " " + last
print(full)
full_1 = f"{first} {last}"
print(full_1)
full_2 = f"{len(first)} {2+2}"
print(full_2)

course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())  # Captialise first letter of each word
# removes white spaces from the start and end of the string value
print(course.strip())
# removes white spaces from the right side of the string value
print(course.rstrip())
# removes white spaces from the left side of the string value
print(course.lstrip())
# returns the index of the first occurrence of the substring
print(course.find("Python"))
# replaces the substring with another substring
print(course.replace("Python", "Java"))
print("pro" in course)  # checks if the substring is present in the string value
# checks if the substring is not present in the string value
print("swift" not in course)
