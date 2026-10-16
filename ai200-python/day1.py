# Week 1, Day 1: Python from Zero
#
# Goal: understand what Python is, set it up, write a first program, and learn
# the basics of variables.
#
# 1. What is Python?
#
# Python is a programming language: a way to tell a computer what to do using
# words that look close to English. It is widely used for AI-200 because Azure
# AI code, SDKs, and examples commonly use Python. Python is also beginner
# friendly: there is less typing, fewer rules, and you can see results quickly.
# You write instructions in a file, and Python reads and runs them from top to
# bottom.
#
# 2. Setup (about 10 minutes)
#
# Install Python:
# - Go to python.org, open Downloads, and install the latest Python 3.
# - On Windows, select "Add python to PATH" during installation.
# - On Mac, you can also run `brew install python` if you have Homebrew.
#
# Install VS Code:
# - Install it from code.visualstudio.com, then install the Python extension.
#
# Check the installation in the VS Code terminal (Terminal > New Terminal):
#     python --version
# You should see a version such as Python 3.12.x. If you see an error, note
# your operating system and the message so you can troubleshoot it.
#
# Create a folder named ai200-python, open it in VS Code, and create day1.py.
#
# 3. Your first program
#
# Run this file with the play button in VS Code or with `python day1.py` in a
# terminal. print() displays text on the screen.
print("Hello, I am learning Python for AI-200!")

# 4. Variables: the most important idea today
#
# A variable is like a labeled box where you store something to use later.
name = "Pramod"
age = 28
is_learning = True

print(name)
print(age)

# The type is inferred from the value:
#   str  - text          - "Pramod"
#   int  - whole number  - 28
#   float - decimal      - 3.5
#   bool - True or False - True
print(type("Pramod"))  # <class 'str'>
print(type(28))        # <class 'int'>
print(type(3.5))       # <class 'float'>
print(type(True))      # <class 'bool'>
print(type(is_learning))

# Variable naming reminders:
# - `=` stores a value; age = 28 puts 28 in the variable named age.
# - Use lowercase and underscores for multiword names: my_name is valid.
# - Names cannot contain spaces or start with a number.
# - Python is case-sensitive: Name and name are different variables.

# F-strings let you insert variables inside braces in a sentence.
print(f"My name is {name} and I am {age} years old.")

# input() always returns text (str), even when the user types a number.
age_text = input("How old are you? ")
print(type(age_text))  # always <class 'str'>

# Convert input to int before doing arithmetic with it.
age_num = int(input("Enter your age as a number: "))
print(f"Next year you will be {age_num + 1}")


# Tasks

# Task 1: Print your name, your city, and your goal in 3 lines.
print("My name is Pramod Kumar. " \
"I am from Atlanta, GA, " \
"and my goal is to clear AI 200 certification by March 2027")

# Task 2: Create language = "Python", hours_per_day = 1, and exam = "AI-200".
# Print a sentence with an f-string about learning Python for one hour per day.
language = "Python"
hours_per_day = 1
exam = "AI-200"

print(f"I am learning {language} everyday for {hours_per_day} hr to clear {exam} certification by March 2027")

# Task 3: Ask for a name and age, convert age to int, and print the age next year.
my_name = input("Type your name: ")
my_age = int(input("Type your age: "))

print(f"Hi {my_name}, next year you will be {my_age+1}.")


# 6. Quick quiz — answer in chat (10 mins)
# 1.What does print() do?
# 2. After x = 5 then x = x + 2, what is x?
# 3. Why does "5" + "3" give "53" and not 8?
# 4. What’s wrong with 1name = "Pramod"?
# 5. What does type(3.5) return?