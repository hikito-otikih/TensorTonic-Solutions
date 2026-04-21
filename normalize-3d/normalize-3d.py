import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v).astype(float)

    if len(v.shape) == 1 :
        return v / np.linalg.norm(v, ord=2)
    Norm = np.expand_dims(np.linalg.norm(v, ord=2, axis=1), axis=1)
    return np.where(Norm == 0, v, v / Norm)