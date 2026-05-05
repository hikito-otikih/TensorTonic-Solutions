import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    y = np.array(y, dtype=int)
    if len(a.shape) < 2 :
        a = np.expand_dims(a, axis=0)
        b = np.expand_dims(b, axis=0)

    dis = np.linalg.norm(a - b, ord=2, axis=1)
    loss = y * dis ** 2 + (1 - y) * np.maximum(0, margin - dis) ** 2
    if reduction=="mean" :
        return np.mean(loss)
    return np.sum(loss)
