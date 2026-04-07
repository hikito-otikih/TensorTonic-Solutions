import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.array(y)
    n = y.size
    _, y = np.unique(y, return_counts=True)
    y = 1.0 * y / n
    y = y.dot(np.log2(y))
    return -y