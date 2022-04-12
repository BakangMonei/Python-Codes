name = input(str("Enter your name: "))
surname = input(str("Enter your surname: "))
gender = input(str("Male or Female: "))
age = input(str('Age: '))
Q1 = input(bool("Is it your first time here? "))
if (Q1 := False):
    print(name + "Welcome")
else:
    print("Please leave" + name)
print("Hi " + name + " " + surname)