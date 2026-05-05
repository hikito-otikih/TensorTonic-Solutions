import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.array(p, dtype=float)
    y = np.array(y, dtype=int)
    py = y * p

    return 1 - (np.sum(py) * 2 + eps) / (np.sum(p) + np.sum(y) + eps)
    