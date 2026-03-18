#04scatterplots-p01Intro.py

import matplotlib.pyplot as pyplot
import random

random.seed(12)
#Scatter plots are used to visualise relationship between two paired sets of data
#Score
score = [random.randint(0,100) for _ in range(30) ]
#Practice time in hours
practice_time = [random.randint(0,12) for _ in range(30) ]
#Player labels
player_labels = [f"P{i}" for i in range(30)]

for x,y in zip(practice_time,score) :
    print(f"({x},{y})")
#Create scatterplot
#Scatter plot syntax : matplotlib.pyplot.scatter(x, y, s=None, c=None, *, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=None, colorizer=None, plotnonfinite=False, data=None, **kwargs)
pyplot.scatter(practice_time, score)

#Add labels to each point using pyplot.annotate()
#matplotlib.pyplot.annotate(text, xy, xytext=None, xycoords='data', textcoords=None, arrowprops=None, annotation_clip=None, **kwargs)
for i,point in enumerate(zip(practice_time,score)) :
    pyplot.annotate(player_labels[i], point, xytext=(5,-5), textcoords='offset points' )
#Here   xaxis = xaxis points
#       yaxis = yaxis points
#       xytext = label offset
#       textcoords = label offset mode

pyplot.show()

