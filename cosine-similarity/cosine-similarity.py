import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)

    dem = (np.linalg.norm(a, ord=2) * np.linalg.norm(b, ord=2))
    if dem == 0 :
        return 0
    return a.dot(b) / dem
    