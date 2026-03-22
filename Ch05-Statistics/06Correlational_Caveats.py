#06Correlational_Caveats.py

#Import python code from files not following python import file naming conventions
import importlib.util

# Specify the filename
filename = "04Correlation.py"
module_name = "correlation"  # Choose a valid module name

# Create a module spec and load it
spec = importlib.util.spec_from_file_location(module_name, filename)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

"""

+----------------------------------+
| Some other Correlational Caveats |
+----------------------------------+
Correlation of 0 indicates that there is no 'linear' relationship between variables. This doesn't mean that the two variables are not related in any way. Two variables may be related but their correlation can be 0 i.e., they are related in a non-linear manner. Example :
    *numbers and their absolute values
"""
import random

random.seed(2)
numbers = [random.randint(-20,20) for _ in range(10)]
absolutes = [-i if i <0 else i for i in numbers]

print(f"numbers :\n{numbers}\nabsolutes :\n{absolutes}")
print(f"correlation = {module.correlation(numbers, absolutes)}")
print()
"""
This relationship between numbers and absolutes cannot be inferred by using the correlation value since the relationship is not a linear one.

Correlation also doesnt tell us anything about how large a relationship is. For example :
"""
values1 = [random.random() for _ in range(10)]
values2 = [i+100 for i in values1]
print(f"numbers :\n{values1}\nabsolutes :\n{values2}")
print(f"correlation = {module.correlation(values1, values2)}")

"""
'values1' and 'values2' are highly correlated but depending on what we are measuring it is possible that the relationship is not very interesting or might be meaningless.
"""
