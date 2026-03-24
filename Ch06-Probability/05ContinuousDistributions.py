#05ContinuousDistributions.py

"""
+--------------------------+
| Continuous Distributions |
+--------------------------+
Coin flip is an example of a discrete distribution - associating positive probability with discrete outcomes.
When modeling distributions we will come across continuous distributions - outcomes are not discrete and are continuous.

For example : Uniform distribution puts equal weight on all numbers between 0 and 1. Since there are infinite numbers between 0 and 1, the weights assigned to each value will be close to zero.
This is why continuous distributions are represented with Probability Density Functions(pdfs).

Probability Density Functions(pdfs) is a mathematical function that describes the likelihood of a continuous random variable taking on a value within a specific range. It is used to model continuous probability distributions.

The PDF does not give the probability of a single exact value (which is zero for continuous variables), but instead provides the relative likelihood of the variable falling within a range of values.
The probability that the variable lies between two values "a" and "b" is given by the area under the PDF curve between those points.

The Cumulative Density Functions(cdfs) give the probability that a random variable is less than or equal to a certain value. It can be thought of as the curve representing the cumulative area of the probability density function for x-axis value less than or equal to a certain point.

"""
