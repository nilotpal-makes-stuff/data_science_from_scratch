#02barcharts-p01Intro.py

#Bar chart - good choice when we need to show how some quantity varies among some discrete set of items
import matplotlib.pyplot

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

bottom = [i-100 for i in gdp]

#Create a bar chart
#Syntax matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
matplotlib.pyplot.bar(years, gdp, width=2, color='red', bottom=bottom)
#Here   x-axis = years
#       y-axis = gdp
#       width = width of bar
#
#Many more customisation options exist

#Add title
matplotlib.pyplot.title("Nominal GDP")

#Add label to x and y axis
matplotlib.pyplot.ylabel("Billions of dollars($)")
matplotlib.pyplot.xlabel("Year")

#display the plot
matplotlib.pyplot.show()

#Matplotlib documentation - https://matplotlib.org

