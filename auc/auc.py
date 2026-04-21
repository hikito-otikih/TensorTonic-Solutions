import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here

    fpr = np.array(fpr).astype(float)
    tpr = np.array(tpr).astype(float)

    fpr = np.delete(fpr, 0) - np.delete(fpr, -1)
    tpr = np.delete(tpr, 0) + np.delete(tpr, -1)

    return np.sum(tpr * fpr) * 0.5