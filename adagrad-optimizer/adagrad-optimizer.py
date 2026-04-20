import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    w = np.array(w).astype(float)
    G = np.array(G).astype(float)
    g = np.array(g).astype(float)
    GT = G + g ** 2
    return (w - lr * g / np.sqrt(GT + eps), GT)