# model_comparison.py

import numpy as np
import statsmodels.api as sm


def fit_model(y, x):
    """
    Fit a linear regression model and return the results object.
    """
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    results = model.fit()
    return results


def compare_models(models):
    """
    Compare multiple models based on AIC, BIC, and R-squared.
    """
    print("Model Comparison:")
    print("Model\tAIC\tBIC\tR-squared")

    for i, model in enumerate(models):
        print(f"Model {i + 1}\t{model.aic:.2f}\t{model.bic:.2f}\t{model.rsquared:.2f}")


if __name__ == "__main__":
    # Sample data
    y = np.array([25.5, 30.1, 27.8, 31.3, 26.1])
    x1 = np.array([1.2, 3.4, 2.8, 4.5, 3.1])
    x2 = np.array([2.5, 1.2, 3.5, 2.1, 4.7])

    # Fit multiple models
    model1 = fit_model(y, x1)
    model2 = fit_model(y, x2)
    model3 = fit_model(y, np.column_stack((x1, x2)))

    # Compare models
    compare_models([model1, model2, model3])
