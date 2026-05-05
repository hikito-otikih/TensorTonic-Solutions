import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    # Write code here
    anchor = np.array(anchor, dtype=float)
    positive = np.array(positive, dtype=float)
    negative = np.array(negative, dtype=float)

    if len(anchor.shape) < 2 :
        anchor = np.expand_dims(anchor, axis=0)
        positive = np.expand_dims(positive, axis=0)
        negative = np.expand_dims(negative, axis=0)

    return np.mean(np.maximum(0, np.sum((anchor - positive)**2, axis=1) - np.sum((anchor - negative)**2, axis=1) + margin))