# Lab 2: Control Statements: select and loops
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
D = int(input("Enter the fourth number: "))
E = int(input("Enter the fifth number: "))

total = A + B + C + D + E
average = total / 5
print("The average is: %d" %(average))

sum = 0
for i in range(5):
    y = int(input("Enter a number: "))
    sum += y
avg = sum / 5
print("The average is %.2f" %(avg))

# EXERCISE 1
A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
BIG = A
if B > BIG:
    BIG = B
elif C > BIG:
    BIG = C
print("the biggest number is %d" %(BIG))

# EXERCISE 2
# Working with control statements IF, IF-ELSE
x = 21
if (x % 20) == 0:
    print("The number is odd.")
else:
    print("The number is even.")

# Printing the grades for certain mark A above 80, between 60-80, and between 50 and 60 "C", below 50 is D
y = 68
if (y < 50):
    print("Your grade is a D")
elif(y < 60):
    print("Your grade is C")
elif(y < 80):
    print("Your grade is B")
else:
    print("Your grade is A")
