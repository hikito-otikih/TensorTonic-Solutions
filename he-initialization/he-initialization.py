import math
import numpy as np
def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here
    L = math.sqrt(6.0 / fan_in)
    return np.array(W).astype(float) * 2 * L - L