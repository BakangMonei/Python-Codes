import random
import string

length = int(input('\n Enter the desired length of your password: '))


lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbol = string.punctuation

# Combining all the data types
all = lower + upper + numbers + symbol

temp = random.sample(all, length)

password = "".join(temp)

print(password)
