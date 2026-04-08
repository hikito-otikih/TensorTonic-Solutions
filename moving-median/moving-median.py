import numpy as np
def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here
    n = len(values)
    idx = n - window_size + 1
    if (idx <= 0) :
        return []
    return [np.median(values[i : i + window_size]) for i in range (idx)]