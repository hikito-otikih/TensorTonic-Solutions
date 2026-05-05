import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.array(y_true, dtype=int)
    y_pred = np.array(y_pred, dtype=float)
    N = y_true.shape[0]
    
    
    return -np.sum(np.log(y_pred[np.arange(N), y_true])) / N