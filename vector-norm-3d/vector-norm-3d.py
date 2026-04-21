import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v = np.array(v).astype(float)
    if len(v.shape) == 1 :
        return np.linalg.norm(v, ord=2)
    return np.linalg.norm(v, ord=2, axis=1)