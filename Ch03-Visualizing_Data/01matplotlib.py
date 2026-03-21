#01matplotlib.py

#Matplotlib - good for simple bar charts, line charts, scatter plots
#import pyplot module in Matplotlib library
import matplotlib.pyplot

#pyplot maintains an internal state in which we build up a visualization step by step.
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#Create a line chart
#Syntax matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
matplotlib.pyplot.plot(years, gdp, color='green', marker='o', linestyle='solid')
#Here   x-axis = years
#       y-axis = gdp
#       color = plot color
#       marker = marker style
#       linestyle = line style
#Many more customisation options exist

#Add title
matplotlib.pyplot.title("Nominal GDP")

#Add label to x and y axis
matplotlib.pyplot.ylabel("Billions of dollars($)")
matplotlib.pyplot.xlabel("Year")

#display the plot
matplotlib.pyplot.show()

#Matplotlib documentation - https://matplotlib.org

