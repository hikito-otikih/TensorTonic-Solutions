import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.array(points)
    centroids = np.array(centroids)

    dis = np.sum((np.expand_dims(points, axis=1) - centroids) ** 2, axis=2)

    return dis.argmin(axis=1).tolist()