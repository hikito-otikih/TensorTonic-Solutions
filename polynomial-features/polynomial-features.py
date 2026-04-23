import numpy as np
def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    values = np.array(values, dtype = float)
    degree = np.array(degree, dtype = int)


    return (np.expand_dims(values, axis=1) ** np.arange(degree + 1)).tolist()