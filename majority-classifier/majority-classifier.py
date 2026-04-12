import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    ma, mi = np.unique(np.array(y_train), return_counts=True)
    return [ma[np.argmax(mi)]] * len(X_test)