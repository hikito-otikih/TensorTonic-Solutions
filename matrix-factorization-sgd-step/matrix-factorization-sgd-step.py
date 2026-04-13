import numpy as np
def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Write code here
    U = np.array(U).astype(float)
    V = np.array(V).astype(float)
    error = r - U.dot(V)
    uv = lr * (error * U - reg * V)
    vu = lr * (error * V - reg * U)
    
    return (U + vu, V + uv)