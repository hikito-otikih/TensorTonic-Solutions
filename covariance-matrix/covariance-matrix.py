import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.array(X).astype(float)
    X = X - np.mean(X, axis=0)
    if X.shape[0] <= 1 or len(X.shape) < 2:
        return None
    return X.T @ X / (X.shape[0] - 1)