def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    for x in X :
        new_x = []
        for i in range(len(x)) :
            for j in range(i + 1, len(x)) :
                new_x.append(x[i] * x[j])
        x += new_x
    return X