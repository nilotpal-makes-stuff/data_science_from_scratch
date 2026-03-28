#01IdeaBehindGradientDescent.py

"""
+----------------------------------+
| The Idea Behind Gradient Descent |
+----------------------------------+

Finding the best model for a certain situation might mean "minimising the error of its predictions" or "maximising the likelihood of the data" - finding maximum or minimum of a function.

Consider some function f which takes in an input vector of real numbers and outputs a single real number.
"""
from typing import List

def sum_of_squares(vector:List[float]) -> float :
    """
    Compute the sum of squared elements in vector
    """
    result = sum([x**2 for x in vector])
    return result

"""
We will need to maximise or minimise a function i.e., we need to find input 'v' which will give us the maximum or the minimum possible value as output.

The gradient (which is a vector of partial derivatives) gives the input direction in which the function most quickly increases.
To maximise a function we pick a random starting point and compute the gradient. Taking a small step towards the gradient we repeat the process with the new starting point.
To minimise a function we pick a random starting point and compute the gradient. Taking a small step opposite to the gradient and we repeat the process with the new starting point.

For functions with one global minimum(or maximum if we are searching for maximum) this procedure will likely find it.
For functions with multiple minima or maxima, we need to run the procedure from multiple starting points to find all the maxima and minima.
For functions with no minima or maxima the procedure goes on forever.
"""
#Display z=x^2 + y^2
import matplotlib.pyplot as pyplot
import numpy

size=10

x = numpy.linspace(-1,1,size)
y = x

#Construct meshgrid - makes 2d array of all possible combinations for x and y
xaxis, yaxis = numpy.meshgrid(x,y)
#zaxis = xaxis^2 + yaxis^2
zaxis = xaxis**2 + yaxis**2
#print(zaxis)

fig, ax = pyplot.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xaxis,yaxis,zaxis)
pyplot.title("Curve : z = x^2 + y^2")
pyplot.show()
