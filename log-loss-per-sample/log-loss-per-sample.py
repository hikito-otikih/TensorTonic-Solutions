import math
import numpy as np

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    y_pred = np.array(y_pred).astype(float)
    y_true = np.array(y_true).astype(float)

    y_pred[np.where(y_pred < eps)] = eps
    y_pred[np.where(y_pred > 1-eps)] = 1-eps
    return (-1.0 * (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))).tolist()