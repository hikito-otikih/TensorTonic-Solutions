import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    x_t = np.array(x_t).astype(float)
    Wx = np.array(Wx).astype(float)
    Wh = np.array(Wh).astype(float)
    b = np.array(b).astype(float)
    h_prev = np.array(h_prev).astype(float)
    return np.tanh(x_t @ Wx + h_prev @ Wh + b)
