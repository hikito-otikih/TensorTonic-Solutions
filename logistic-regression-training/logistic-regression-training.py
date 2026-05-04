import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    N = X.shape[0]
    W = np.zeros(X.shape[1])
    B = 0
    for i in range(steps) :
        p = _sigmoid(X.dot(W) + B)
        dB = (-1/N * (y * (1 - p) - (1 - y) * p))
        dW = np.expand_dims(dB, axis=1) * X
        dB = np.sum(dB)
        dW = np.sum(dW, axis=0)
        W -= dW * lr
        B -= dB * lr

    return W, B
