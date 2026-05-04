import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    ax = len(x.shape)
    if ax > 1 :
        x = np.exp(x - np.expand_dims(np.max(x, axis = ax - 1), axis = ax - 1))
        return x / np.expand_dims(np.sum(x, axis = 1), axis = 1)
    x = np.exp(x - np.max(x, axis = ax - 1))
    return x / np.sum(x)