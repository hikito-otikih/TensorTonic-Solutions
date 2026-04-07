import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    x = np.array(x) * 1.0
    idx = np.where(x < 0)
    x[idx] = alpha * (np.exp(x[idx]) - 1)
    return x.tolist()