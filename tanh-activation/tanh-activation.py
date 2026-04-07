import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.array(x)
    ex = np.exp(x)
    emx = 1 / ex
    return (ex - emx) / (ex + emx)