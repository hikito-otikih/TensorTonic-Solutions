import numpy as np
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    x1 = np.array(x1).astype(float)
    x2 = np.array(x2).astype(float)
    cos12 = x1.dot(x2) / (np.sqrt(x1.dot(x1)) * np.sqrt(x2.dot(x2)))
    L = 1 - cos12
    if label == -1 :
        L = max(0.0, cos12 - margin)
    return L
        