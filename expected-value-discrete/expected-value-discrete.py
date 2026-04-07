import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x)
    p = np.array(p)

    if p.sum() != 1:
        raise ValueError
    
    if x.size == 0:
        return 0.0
    
    return float(x.dot(p))
