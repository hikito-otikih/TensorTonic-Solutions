import numpy as np
def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here
    values = np.array(values, dtype=float)
    weights = np.array(weights, dtype=float)
    N = len(values)
    M = len(weights)
    S = np.sum(weights)
    return [values[i : i + M].dot(weights) / S for i in range(N - M + 1)]