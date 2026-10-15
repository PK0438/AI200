# print statement
print("Hello, I am learning python for AI 200")

# A few rules that trip up beginners:
# 1. = means “store this in that box”, not math equals. age = 28 means put 28 in the box labeled age.
# 2. Names: lowercase, use _ for spaces, can’t start with a number. my_name is good, my name and 1name are not. Python cares about capital letters: Name and name are different boxes.
# 3. Python figures out the type automatically:

# variable declaration and printing
name = "Pramod"
age = 32
is_learning = True
height = 5.4

print(name)
print(age)

# type of the variable
print(type(name))
print(type(age))
print(type(is_learning))
print(type(height))

# f-strings
# The f in front lets you drop variables inside { }.

print(f"I am {name} and I am {age} years old")

# input - TRAP
age_text = input("How old are you?")
print(age_text)
print(type(age_text))       # should be str

#input() always gives you text, even if you type a number. To do math, convert it:

age_num = int(input("How old are you?"))
print(age_num)
print(type(age_num))


## Task 1: Print your name, your city, and your goal in 3 lines.
print("My name is Pramod Kumar. " \
"I am from Atlanta, GA, " \
"and my goal is to clear AI 200 certification by March 2027")

## Task 2: Create 3 variables — language = "Python", hours_per_day = 1, exam = "AI-200" — and print one sentence with an f-string: “I am learning Python for 1 hour per day for AI-200.”

language = "Python"
hours_per_day = 1
exam = "AI-200"

print(f"I am learning {language} everyday for {hours_per_day} hr to clear {exam} certification by March 2027")

## Task 3: Ask for name and age with input(), convert age to int, and print: “Hi [name], next year you will be [age+1].”

my_name = input("Type your name: ")
my_age = int(input("Type your age: "))

print(f"Hi {my_name}, next year you will be {my_age+1}.")