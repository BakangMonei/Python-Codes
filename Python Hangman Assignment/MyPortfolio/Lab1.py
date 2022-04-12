# LAB 1
# variable declarations
a = 23
b = 12
c = 2.402
name = "Tshepo"
Surname = "Gobonamang"

# Basic Operators
full_name = name + Surname # concatenate strings
sum = a + b
product = a * b
sumth = a**b # exponent
bb = b**2
divc = a / b
subtrct = a - b
divs = a%b

# ACTIVITY 1
# Assignment Operators
c += b
d = e = f = g = h = i = 5
d -= 12
e *= 0.5
f /= 2
g **= 2
h %= 3
i //= d

# ACTIVITY 2
# Comparison Operators
a == b
b != d # ! =
a < c
i > d
a <= 9
b >= b

# ACTIVITY 3
print(a==b)
print(b != d)
print(a < c)
print(i > d)
print(a <= 9)
print(b >= b)

# Logical Operators
# ACTIVITY 4
print(True and True)
print(True or False)
print(True and False)
print(True and not False)

# string Operators
var1, var2, var3 = "Tshepo", "Gobonamang", "I Love Python"
print(var1 + " " + var2)
print(var3 * 2)
print(var3[:6] + " " + var1)
print(var2 + " " + var3[2:])
print("lov" in var3)
print("lov" in var2)
print("lov" not in var3)
print("lov" not in var2)

# ACTIVITY 5
# A code that calculates area of a circle and working with user inputs
var4 = input("Enter the value of the radius: ") # input expect a string
carea = 3.142 * int(var4) * 2 # Cast that string into an integer
print("The area of the circle is: %d" %(carea))

# Calculating a simple interest
rate, principal_amount, time = 0.03, 28000, 6
si = principal_amount * rate * time
print("The simple interest of %d for %d years at %d percent, is %2f" % (principal_amount, time, (100 * rate), si))

# EXERCISE 1
centigrade= float(input('Please enter temperature in : '))
fahrenheit = round((centigrade * 1.8) + 32, 1)
print("The temperature in Fahrenheit is %d°F" %(fahrenheit))

#temp from Fahrenheit to centigrade
fahrenheit = float(input("Please enter temperature in °F: "))
centigrade = round((fahrenheit - 32) / 1.8, 1)
print("The temperature in Centigrade is %d " %(centigrade))

