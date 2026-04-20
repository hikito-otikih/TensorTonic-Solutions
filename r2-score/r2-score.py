import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_mu = np.expand_dims(np.mean(y_true), axis=0)
    num = np.sum((y_true - y_pred) ** 2)
    dem = np.sum((y_true - y_mu) ** 2)
    if dem == 0 :
        return num == 0
    return 1 - num / dem