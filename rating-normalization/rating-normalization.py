import numpy as np
def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    matrix = np.array(matrix, dtype=float)
    bool_mat = matrix != 0
    me = np.sum(matrix, axis=1)
    length = np.sum(bool_mat, axis=1)
    me = np.expand_dims(np.where(length != 0, me / length, 0), axis=1)
    return np.where(me != 0, matrix - me * bool_mat, matrix).tolist()
    
    