# LAB 4 ACTIVITY 1
import os
print(os.getcwd())
print(os.listdir())
os.chdir('C:\\Users\\cse20-018\\Desktop\\Portfolio\\testing images')
with open('1.txt', 'r') as f:
    data = f.read()
print(data)
with open ('1.txt', 'w') as f:
    data = 'This is fantastic, Python \n Programming is really fun'
    f.write(data)
with open('1.txt', 'r') as f:
    data = f.read()
print(data)

# ACTIVITY 2: The statement was added to the 1.txt file
# Exercise 1
# Python program to
# demonstrate merging
# of two files

data = data2 = ""

# Reading data from file1
with open('File1.txt') as fp:
    data = fp.read()

# Reading data from file2
with open('File2.txt') as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

with open('File3.txt', 'w') as fp:
    fp.write(data)