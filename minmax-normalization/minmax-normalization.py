import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X).astype(float)
    x_max = np.expand_dims(np.max(X, axis=axis), axis=axis)
    x_min = np.expand_dims(np.min(X, axis=axis), axis=axis)

    return (X - x_min) / (x_max - x_min + eps)
    