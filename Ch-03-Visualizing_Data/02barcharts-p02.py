#02barcharts.py

#Bar chart - Can also be used to plot histograms of bucketed numeric values
# Useful for visually exploring how values are distributed
from collections import Counter
import random
import matplotlib.pyplot as pyplot

#set seed
random.seed(10)

#Grades
grades = [random.randint(0,100) for i in range(200)]
print(f"Grades = {grades}")

#Frequency of grades in range
#min(grade//10, 90) -  converts score 100 into 90
histogram = Counter(min(grade//10, 90) for grade in grades)
print(histogram)

#Create a bar chart
#Syntax : matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
pyplot.bar([x*10 for x in histogram.keys()], histogram.values(), width=8, color='red', edgecolor=(0,0,0))
#Here   x-axis = years
#       y-axis = gdp
#       width = width of bar
#       edgecolor = color of edge
#Many more customisation options exist

pyplot.bar([x*10+1 for x in histogram.keys()], histogram.values(), width=4, color='blue', edgecolor=(0,0,0))

#axis sets start end points for x and y axis
#Syntax : matplotlib.pyplot.axis(arg=None, /, *, emit=True, **kwargs)
# / in function definition says that only positional arguments allowed for parameters before '/' symbol
# * in function definition says that only keyword arguments allowed for parameters after '*' symbol
pyplot.axis([-5,105,0,50])
# [xstart, xstop, ystart, ystop]

#define ticks for x axis
pyplot.xticks([x*10 for x in range(11)])

#Add title
pyplot.title("Scores Distribution")

#Add label to x and y axis
pyplot.ylabel("Number of students")
pyplot.xlabel("Score")

#display the plot
pyplot.show()

#Matplotlib documentation - https://matplotlib.org

