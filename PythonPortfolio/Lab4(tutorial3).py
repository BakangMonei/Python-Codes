# LAB 4: Directories & Working with Files
import os, shutil
print(os.getcwd()) # Prints the current working directories
os.chdir('C:\\Users\\cse20-018\\Desktop') # Change the current working dictionary
print(os.getcwd())
os.chdir('C:\\Users\\cse20-018\\Desktop\\Portfolio') # getting back to where we were
print(os.getcwd())
print(os.listdir()) # lists all the subdirectories and files in the current
print(os.listdir('C:\\Users'))
# os.mkdir('training images') # Creating a new file called IMAGES
print(os.listdir())
os.rename('images', 'testing images') # renames images to testing images
os.rmdir('JE') # this function only works if you want to remove empty directories
print(os.listdir())
shutil.rmtree('training images') # Used to delete directories with files or anything inside them