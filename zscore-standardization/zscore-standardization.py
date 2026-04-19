import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.array(X).astype(float)
    mean_x = np.expand_dims(np.mean(X, axis=axis), axis=axis)
    std_x = np.expand_dims(np.std(X, axis=axis), axis=axis) + eps
    return (X - mean_x) / std_x