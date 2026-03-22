#05Simpsons_paradox.py

"""
+-------------------+
| Simpson's Paradox |
+-------------------+
Simpsons paradox - correlations can be misleading when 'confounding variables' are ignored.
Confounding variables are variables that are associated with both the exposure (independent variable) and the outcome (dependent variable) in a study, potentially distorting the apparent relationship between them.

This phenomenon is seen often in the real world. The key issue is that correlation measures the relationship between two variables all else being equal. When there is a deeper pattern to the class assignments, 'all else being equal' is a bad assumption and thus correlation gives us incorrect conclusions.

This can be avoided by knowing the data we are working on and identifying and excluding the possible confounding factors from correlation computation.

Example case of this is :
In a study linking ice cream sales to sunburns, temperature is a confounder — higher temperatures increases ice cream consumption and increases the chance of getting a sunburn. A correlation between icecream sales and sunburns will be high indicating positive correlation but these variables are not correlated, they are each correlated to the temperature factor.
"""
