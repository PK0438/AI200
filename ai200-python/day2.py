# Day 2: Conditions and comparison operators

# 1. Comparison operators ask a question and return True or False.
print("Comparison operators:")
print(5 == 5)    # == equal to: True
print(5 != 6)    # != not equal to: True
print(10 > 5)    # > greater than: True
print(10 < 5)    # < less than: False
print(18 >= 18)  # >= greater than or equal to: True
print(17 <= 18)  # <= less than or equal to: True

# The big trap:
# = stores a value. For example, age = 28 stores 28 in age.
# == compares values. For example, age == 28 asks whether age is 28.
# An if condition needs a question, so `if age = 28:` is invalid Python.


# 2. if / elif / else
# A colon ends each branch header. Indent the branch body by 4 spaces.
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# elif means "otherwise, check this next." You can use multiple elif branches.
score = 85

if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Need more practice")

# Python runs only the first branch whose condition is True.
# Check the highest score first; if score >= 60 came first, an 85 would get Grade C.
# else has no condition: it runs only if none of the earlier conditions were True.
# Python uses indentation to group branch bodies (usually 4 spaces), not braces.
# Use `elif`, not `else if`.


# 3. Logical operators combine or change questions.
# and: both conditions must be True.
# or: at least one condition must be True.
# not: flips True to False, or False to True.
age = 20
score = 70

if age >= 18 and score >= 60:
    print("Eligible")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")

is_raining = False
if not is_raining:
    print("Go outside")


# 4. Common errors to watch for
# - Forgetting the colon: `if age >= 18` should end with `:`.
# - Mixing tabs and spaces or indenting branches unevenly can cause errors
#   or make code run in the wrong branch.
# - Using = instead of == in a condition.
# - Writing `else if` instead of `elif`.
# - input() returns text. Convert it before comparing it with a number:
#   age_from_input = int(input("How old are you? "))
#   if age_from_input >= 18:
#       print("You are an adult.")
# Comparing the text "18" with the number 18 raises a TypeError.

# Task 1 — if / else: 
# Ask age with int(input(...)). If age >= 18 print “You are an adult.” else print “You are a minor.”

age = int(input("How old are you: "))

if age >=18:
    print("You are an adult!")
else:
    print("You are a minor.")


# Task 2 — elif chain:
# Ask exam score 0-100. If >= 90 print “Grade A”, elif >= 75 “Grade B”, elif >= 60 “Grade C”, else “Need more practice”. Test it twice — once with 85, once with 45. What do you get each time?

score = int(input("What's your score: "))

if score >= 90: 
    print("Grade A")
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Needs more practice.")

# 45 score - Needs more practice
# 85 score - Grade B

# Task 3 — combining Day 1 + Day 2:
# Ask name, age, and score. If age >= 18 and score >= 60 print f"Hi {name}, you are eligible." else print f"Hi {name}, not eligible yet.

name = input("Name: ")
age = int(input("Age: "))
score = int(input("Score: "))

if age >= 18 and score >= 60:
    print(f"Hi {name}, you are eligible.")
else:
    print(f"Hi {name}, not eligible yet.")


# 6. Quick quiz — answer in chat (10 mins)
# 1. What is the difference between = and ==?
# 2. What happens if you forget the : after if age >= 18?
# 3. After x = 10, what does this print? if x > 5: print("big") else: print("small")
# 4. What is True and False? What is True or False?
# 5. Why does indentation matter in Python? What error can wrong indentation cause?