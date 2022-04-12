# Lab 3: Lists, Tuples, Dictionaries and their operations
print('Lab 3: Lists, Tuples, Dictionaries and their operations')

# Lists
l1 = [2,3,4,53,5,78,100, 12, -1] # list 1 declaration of same datatype
l2 = ["Segomotso", "Ruth"," ", "Amantle", "Thabile"] # String datatype declarations
l3 = ['a', 3, 43, 'b', 'c', 103, 'd', 'e', 'Thabang'] # Mixed datatype declarations
l4 = l2 + l3 # Concatenating two lists, list 2 and list 3
print(l4)
print(len(l1)) # Getting the length and of the list and printing it
print(l2[0]*l1[3]) # Accessing the members of my lists


if "Segomotso" in l2:       # Membership functions using *SELECT STATEMENT*
    print("Segomotso is part of list")

for i in l2:                # Using loops to print members of the list
    print(i)

for i in l1:
    print(i)

# Tuples
t0 = ()
t1 = (2, "Kitso", 3, 4, 6, "Jason")
t2 = ("Jane", 2.178, 2, 12, "Masego")

print(t1[1] + " " + t2[-1]) # Tuples and Concatenating from different tuples
print(t1 + t2) # Concatenating 2 tuples

print(len(t1) + len(t2)) # Prints the sum of length of the 2 tuples
# del(t1[5])
# Cannot delete object deletion in tuples

for i in t1:
    print(i)

# Exercise 1: Writing a code that access value 20 from the "aTuple"
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

# Exercise 2: An example of tuple unpacking.

# Sets
s0 = 'William Winnie' # Setting a String
s01 = list(s0) # Constructing a list from a String
s02 = set(s0) # Constructing a set from a String
s00 = set() # Defines/declares an empty set
s1 = {} # Defines an empty dictionary
s2 = {'Baseki', 'Resego', 'Rebaone', 'Stewart', 'Baseki', 'baseki', (3, 4, 11, 4)}
# tuple1s2 = (3, 4, 11, 4)
s3 = {'Stewart', 'PM', 1, 55.28, ('bida', 'cse', 'abc'), 'Resego'}

print(s00|s2)
print(s2.union(s3)) # Try this print(s2.union(s3))
print(s2&s3)
print(len(s3)) # Prints the length of s3
print(s01)
print(s02)

if 'cse' in s3:         # Membership function in set3
    print("cse is a member of set3")

else:
    print("CSE is NOT a member of set3")

# Add a FULL FROZEN SET code

# DICTIONARIES
d1 = dict([
    ('Name', 'Segomotso'),
    ('Surname', 'Isaac'),
    ('ID', '21309'),
    ('is_a', 'Lecture'),
    ('Location', 'Palapye'),
    ('School', 'SCIS'),
    ('Gender','Female')
])

d2 = dict(      # Declaring a dictionary by stating the <keys>
    corse_name = 'BIDA',
    venue_at = 'Lecture Theater',
    max_number = 60,
    resourcesneeded = ('Laptop', 'Pen', 'Notebook')
)

d3 = {'ID':'ict-003', 'IS': 50, 'AWD': 78, 'IDA': 41}
up3 = {'IS': 75, 'IDA': 82} # A new list
d3.update(up3) # Update d3

# Accessing dictionary contents note that the key value is important
print(d1['is_a'])
print(d2['resourcesneeded'])
print(d3['IDA'])

# Exercise 3: Use update to add a new key to d1 called siblings and the values must be a list of 4 strings. i.e. Names of the siblings and access the 3rd element of that string and display it.
d1 = dict([
    ('Name', 'Segomotso'),
    ('Surname', 'Isaac'),
    ('ID', '21309'),
    ('is_a', 'Lecture'),
    ('Location', 'Palapye'),
    ('School', 'SCIS'),
    ('Gender','Female'),
    ('Siblings','Ruth')
])
up1 = {'Siblings', 'Ruth'}
d1.update(up1)