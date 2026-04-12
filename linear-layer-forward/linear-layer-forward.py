import numpy as np
def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    return (np.array(X).astype(float) @ np.array(W).astype(float) + np.array(b).astype(float)).tolist()
    