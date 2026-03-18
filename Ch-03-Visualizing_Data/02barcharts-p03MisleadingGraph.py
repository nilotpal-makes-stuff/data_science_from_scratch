#02barcharts-p03MisleadingGraph.py

#Bar charts can be misleading if the y-axis does not start from 0
import matplotlib.pyplot as pyplot

units_sold = [500, 490, 507, 505, 505]
month = ["Jan", "Feb", "March", "April", "May"]

#Create a bar chart
#Syntax : matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
pyplot.bar(month, units_sold, color='red', edgecolor=(0,0,0))
#Here   x-axis = month
#       y-axis = units_sold
#       width = width of bar
#       edgecolor = color of edge
#Many more customisation options exist

#Misleading axis
pyplot.axis(ymin=(min(units_sold)-2))

#Add title
pyplot.title("Units Sold in 2025(Misleading graph)")

#Add label to x and y axis
pyplot.ylabel("Number of units sold -->")
pyplot.xlabel("Month -->")

#display the plot
pyplot.show()

#For the above graph it appears that there is huge variations in units sold while that is not true.
#A better graph which represents the accurate picture :
pyplot.bar(month, units_sold, color='green', edgecolor=(0,0,0))

#Add title
pyplot.title("Units Sold in 2025(Correct graph)")

#Add label to x and y axis
pyplot.ylabel("Number of units sold -->")
pyplot.xlabel("Month -->")

#display the plot
pyplot.show()

#Matplotlib documentation - https://matplotlib.org

