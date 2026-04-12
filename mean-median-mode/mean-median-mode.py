
import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    y = Counter(x)
    x = np.array(x).astype(float)
    a, b = y.most_common(1)[0]
    return (np.mean(x), np.median(x), a)