# Lab 3: Lists, Tuples, Dictionaries and their operations
l1 = [2, 3, 4.53, 5, 78, 12, -1] # List 1, declaring same data types
l2 = ["Tshepo", "Kitso", " ", "Nkosi", "Sethunya"] # string data types declarations
l3 = ['a', 3, 43, 'b', 'c', 103, 'd', 'e', 'Thabiso'] # mixed data types declarations
l4 = l2 + l3 # concatenating 2 lists
print(l4)
print(len(l1)) # Getting the length of the list and printing it
print(l2[0] * l1[3]) # Accessing the members of your list

if "Tshepo" in l2: # Membership functions using a select statement
    print("Tshepo is a member of the list!")
else:
    print("Tshepo is not part of the list!")

for i in l2: # Using loops to print members of a list
    print(i)

for i in l1:
    print(i)

# TUPLES
t0 = ()
t1 = (2, "Kitso", 3, 4, 6, "Jason")
t2 = ("Jane", 2.178, 2, 12, "Masego")

print(t1[1] + " " + t2[-1]) # tuples and concatenating from different tuples
print(t1 + t2) # concatenating two tuples

print(len(t1) + len(t2)) # prints the sum of the length of the two tuples
# del(t1[5]) # Cannot delete object deletion in tuples
print(len(t1))

for i in t1:
    print(i)

# EXERCISE 1
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

# EXERCISE 2
# Here we create a tuple from a list:
tuple([561, 1105, 1729, 2465])
(561, 1105, 1729, 2465)

# create a tuple containing the characters of a string:
tuple("Carmichael")
('C', 'a', 'r', 'm', 'i', 'c', 'h', 'a', 'e', 'l')

#  we can test for membership using the in operator:
5 in (3, 5, 17, 257, 65537) # TRUE

# Tuple unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# SETS
s0 = 'William Winnie' # setting a string
s01 = list(s0) # constructing a list from a string i.e. character list
s02 = set(s0) # constructing a set from a string
s00 = set() # defines/declares an empty set
s1 = set # defines an empty dictionary
s2 = {'baseki', 'Resego', 'Rebaone', 'Stewart', 'Baseki', 'baseki'}
s3 = {'Stewart', 'PM', 1, 55.28, None, ('bida', 'cse', 'abc'), 'Resego'}

print(s00|s2)
print(s2.union(s3)) # try this print(s2|s3)
print(s2|s3)
print(len(s3))
print(s01)
print(s02)
if 'cse' in s3: # Membership function in s3
    print("cse is a member of set 3")
else:
    print("cse is NOT a member of set 3")

# DICTIONARIES
d1 = dict([ # declaring a dictionary by stating the <key>
    ('name', 'Tshepo'),
    ('surname', 'Gobonamang'),
    ('ID', '21309'),
    ('is_a', 'Lecturer'),
    ('location', 'Tlokweng'),
    ('school', 'SCIS'),
    ('gender', 'Male')
])

d2 = dict( # Another way of declaring a dictionary
    course_name = 'bida',
    venue_at = 'lecturer theater',
    max_number = 60,
    resources_needed = ('laptop', 'pen', 'notebook')
)

d3 = {'ID':'ict-003', 'IS': 50, 'AWD': 78, 'IDA': 41} # Yet another method of declaring a dictionary

up3 = {'IS': 75, 'IDA': 82} # A new list
d3.update(up3) # update d3

# Accessing dictionary contents note that the key value is important
print(d1['is_a'])
print(d2['resources_needed'])
print(d3['IDA'])

# EXERCISE 3
up1 = {'siblings': 'Sego'}
d1.update(up1)
print(d1['siblings'])