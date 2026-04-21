import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x).astype(float)
    var = np.sum((x - np.mean(x)) ** 2) / (x.size - 1)
    return (var, np.sqrt(var))