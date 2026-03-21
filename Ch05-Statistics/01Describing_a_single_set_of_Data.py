#01Describing_a_single_set_of_Data.py

"""
+---------------------------------+
| Describing a Single Set of Data |
+---------------------------------+
Statistics refers to mathermatics and techniques with which we understand data.

One obvious description of a dataset is the data itself.
"""
import random

height_rng = (150,190)
#Generate random heights in centimeters(cm)
random.seed(12)
heights = [random.random() for _ in range(100)]
heights = [int(h*(height_rng[1]-height_rng[0])+height_rng[0]) for h in heights]
print(f"Heights data : {heights}")

"""
For small datasets, data is the best description.
For large datasets, data is unweildy and opaque - not easy to get insights from.

We use statistics to distil and communicate relevant features of data.

Simplest statistic is the number of data points also referred to as 'count' :
"""
print(f'Count : {len(heights)}')

"""
We can also check the smallest and the largest values in a dataset which are referred to as maximum and minimum values.
"""
print(f'Maximum value : {max(heights)}')
print(f'Minimum value : {min(heights)}')

"""
We can also obtain special cases like the second smallest and the second largest values in a dataset.
"""
heights_sorted = sorted(heights)
print(f'Second largest value : {heights_sorted[-2]}')
print(f'Second smallest value : {heights_sorted[1]}')


