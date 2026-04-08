name = input("What is your name? ")
age = input("How old are you? ")
Fcolor = input("What is your favorite color? ")

try:
    age = int(age)
except ValueError:
    print("Please enter a valid number for age.")
    age = input("How old are you? ")
    try:
        age = int(age)
    except ValueError:
        print("Invalid input for age. Setting age to 0.")
        age = 0

try:
    name = str(name)
except ValueError:
    print("Invalid input for name.")
    name = "Unknown"

try:
    Fcolor = str(Fcolor)
except ValueError:
    print("Invalid input for favorite color.")
    Fcolor = "Unknown"

Output = f"Your name is {name}, you are {age} years old, and your favorite color is {Fcolor}."
print(Output)
