import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    diff = np.array(y_true).astype(float) - np.array(y_pred).astype(float)
    return np.where(np.abs(diff) <= delta, 0.5 * diff ** 2, delta * (np.abs(diff) - 0.5 * delta)).mean()