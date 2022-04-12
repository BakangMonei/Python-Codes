# LAB 5: Functions
def hello(): # function no return type no argument passing
    print("Hello World")

def do_operations(num1, num2): # Function passes arguments and returns a type
    s = num1 + num2
    sub = num1 - num2
    d = num1 / num2
    r = num1 % num2
    m = num1 * num2
    ex = num1 ** num2
    return s, sub, d, r, m, ex # Returns a tuple

def multiplicationLineColumn(line, column):
    try:
        sizeLine = len(line)
        sizeColumn = len(column)
        if(sizeLine != sizeColumn):
            raise ValueError("Exception")
        res = sum([line[i] * column[i] for i in range(sizeLine)])
        return res
    except ValueError:
        print("You should have the same len line and column!!")

def getColumn(matrix, numColumn):
    size = len(matrix)
    column = [matrix[i][numColumn] for i in range(size)]
    return column
def getLine(matrix, numLine):
    line = matrix[numLine]
    return line

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Second matrix/list
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Second matrix/list
matrix = [] # An empty matrix will be updated

for i in range(len(A)):
    matrix.append([])
    for j in range (len(B)):
        matrix[i].append(multiplicationLineColumn(getLine(A, i), getColumn(B, j)))
print(matrix)

print("Detailed Report!")
print("Rows multiply each columns in each set")