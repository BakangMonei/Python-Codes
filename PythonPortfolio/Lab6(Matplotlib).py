# Lab 6: Introduction to Numpy, matplotlib, pandas. (Big Data Processing)
# Activity 1
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Drawing the cartesian plane, and its coordinates
ax.plot([1, 2, 3, 4], [1, 4, 2,3])
# y-axis
plt.ylabel('y values')
# x-axis
plt.xlabel('x values')
fig.show()
plt.show()
# declaration of data
names = ['Nametso', 'Lerato', 'Lesedi', 'Plaatjies']
# Student Marks
scores = [60, 40, 20, 89]
# Grid Sizes
plt.figure(figsize=(6,3))
plt.subplot(131)
# Three bar graphs will be produced
plt.bar(names, scores)
plt.subplot(132)
plt.bar(names, scores)
plt.subplot(133)
plt.bar(names, scores)
plt.suptitle("Student's marks")
plt.show()
output = "The results are (1, 1), (2, 4), (3, 2) and (4, 3)"
print(output)