import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    n = len(y_pred)
    y_pred = np.array(y_pred).astype(float)
    y_true = np.array(y_true).astype(float)
    return np.sum((y_pred - y_true) ** 2) / n
