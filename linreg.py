import numpy as np
import statsmodels.api as sm

def perform_simple_linear_regression(y, x):
    if len(y) != len(x):
        return "Error: # of elements in dependent + independent variables must be the same."

    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    return str(results.summary())
