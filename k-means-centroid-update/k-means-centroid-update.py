import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    # Write code here
    points = np.array(points)
    centroid = np.zeros((k, points.shape[1]))
    cnt = np.zeros(k)
    for i, point in enumerate(points) :
        centroid[assignments[i]] += point
        cnt[assignments[i]] += 1
    print(centroid)
    valid_ind = np.where(cnt != 0)
    centroid[valid_ind] /= np.expand_dims(cnt[valid_ind], axis=1)
    return centroid.tolist()