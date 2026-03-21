#03linecharts.py

import matplotlib.pyplot as pyplot

#Line charts are good for displaying trends
variance = [2**x for x in range(10)]
bias_squared = variance[-1::-1]

#print(variance)
#print(bias)

total_error = [x+y for x,y in zip(variance, bias_squared)]
xs = [i for i,_ in enumerate(variance)]

#We can plot multiple graphs in the same figure if we plot them before pyplot.show() method
#plot Syntax : matplotlib.pyplot.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
pyplot.plot(xs, variance, 'g-', label='variance')
#Here   xaxis = xs
#       yaxis = variance
#       linestyle = 'g-' - indicates green solid line
#       label = 'variance' - sets label for the plot
pyplot.plot(xs, bias_squared, 'r-.', label='bias^2')
pyplot.plot(xs, total_error, 'b:', label='total error')
#       linestyle = 'r-.' Red dot-dashed line
#       linestyle = 'b:' Blue dotted line

#legend() displays legend for the graph
#Syntax : matplotlib.pyplot.legend(*args, **kwargs)
pyplot.legend(loc=9)
#loc=9 - sets legend on top-center location

pyplot.xlabel("Model complexity")
pyplot.xticks([])
pyplot.title("Bias-Variance Tradeoff")

#Display graph
pyplot.show()
