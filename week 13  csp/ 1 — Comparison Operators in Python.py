# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4
print(a) #output 3
print(b) #output 4
print(a == b) #output False


print(a == b)   # checks for equality # False
print(a != b)   # checks if is not equal # True
print(a > b)    # checks for greater than # False
print(a < b)    # checks for less than # True
print(a >= b)   # checks for greater than or equal to # False
print(a <= b)   # checks for less than or equal to # True


#predict the output of the following comparisons:
10 > 5 # true
7 == 2 * 3 + 1 # true
8 != 8 # false
4 <= 2 + 2 # true

# Write 3 examples that result in True and 3 that result in False.

x = 10
y = 20
print(x == y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)
print(x != y)

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"

score = int(input("What is your test score?"))
# make this program for all grading spectrums
# if the score is between 90 - 100... you got an A
# if the score is between 80 - 89... you got an B
# if the score is between 70 - 79... you got an C
# if the score is between 61 - 69... you got an D 
# else you failed
if score >= 60:
    print("You passed the test.")
else:
    print("You didn't pass.")


grade = int(input("What is your current grade?: "))

# if the score is between 90 - 100... you got an A
if grade >= 90 and grade <= 100:
    print("Your current grade is an A.")

# if the score is between 80 - 89... you got an B
elif grade >= 80 and grade <= 89:
    print("Your current grade is an B.")

# if the score is between 70 - 79... you got an C
elif grade >= 70 and grade <= 79:
    print("Your current grade is an C.")

# if the score is between 61 - 69... you got an D 
elif grade >= 60 and grade <= 69:
    print("Your current grade is an D.")
else: 
    print("Your current grade is an F.")






# ask for a password
# print:
password = input("What is your password? ")

