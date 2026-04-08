import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)
    m = rater1.size
    p0 = np.sum(rater1 == rater2) * 1.0 / m
    rater1 = np.bincount(rater1).astype(float)
    rater2 = np.bincount(rater2).astype(float)
    n = max(rater1.size, rater2.size)
    np.pad(rater1, (0, n - rater1.size), mode="constant", constant_values=0)
    np.pad(rater2, (0, n - rater2.size), mode="constant", constant_values=0)
    pe = rater1.dot(rater2) / m ** 2
    if pe == 1:
        return 1
    return (p0 - pe) / (1 - pe)