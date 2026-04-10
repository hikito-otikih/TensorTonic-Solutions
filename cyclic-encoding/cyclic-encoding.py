import numpy as np
import math
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    values = np.array(values)
    theta = 2 * math.pi * values / period
    encoded = np.vstack((np.sin(theta), np.cos(theta))).T
    return encoded.tolist()