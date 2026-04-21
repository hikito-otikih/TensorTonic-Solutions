import numpy as np
def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    values = np.array(values, dtype=float)
    key, idx, freq = np.unique(values, return_counts=True, return_inverse=True)
    less_than_counts = np.insert(np.cumsum(freq[:-1]), 0, 0)
    avg_rank_uniques = less_than_counts + (freq + 1) / 2.0
    return avg_rank_uniques[idx].tolist()

    
    