#04scatterplots-p02MisleadingGraph.py

import matplotlib.pyplot as pyplot
import random

random.seed(12)
#Scatter plots automatically choses scale for the x,y axis in graph
#This can lead to creation of misleading visualisations
#Score
score = [random.randint(70,100) for _ in range(30) ]
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

#This scatter plot shows a misleading visualisation, values are scattered more then they actually are
pyplot.title("Score vs Practice time (Misleading representation)")
pyplot.xlabel("Practice time -->")
pyplot.ylabel("Score -->")
pyplot.show()

#Use scaling to obtain proper visualisations which represent the data accurately
pyplot.scatter(practice_time, score)
pyplot.axis([-5,max(practice_time)+5, -5,max(score)+5])

#labels
for i,point in enumerate(zip(practice_time,score)) :
    pyplot.annotate(player_labels[i], point, xytext=(5,-5), textcoords='offset points' )

#display
pyplot.title("Score vs Practice time (Correct representation)")
pyplot.xlabel("Practice time -->")
pyplot.ylabel("Score -->")
pyplot.show()

#matplotlib docs = https://matplotlib.org/gallery.html
#seaborn - allows for more complex visualizations - https://seaborn.pydata.org
#altair - newer python library for declarative visualizations - https://altair-viz.github.io
#bokeh - library which brings D3 style visualizations to python
