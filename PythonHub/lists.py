# Python program to find sum of elements in list
total = 0

# creating a list
list1 = [1, 2, 3, 4, 5]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
    total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)