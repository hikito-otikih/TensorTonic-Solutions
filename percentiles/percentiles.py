import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x = np.array(x).astype(float)
    q = np.array(q).astype(float)
    return np.quantile(x, q / 100)