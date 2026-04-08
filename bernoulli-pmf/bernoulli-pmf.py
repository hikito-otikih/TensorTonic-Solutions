import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.array(x) * 1.0
    return (np.where(x == 1, p, 1-p), p, p * (1 - p))