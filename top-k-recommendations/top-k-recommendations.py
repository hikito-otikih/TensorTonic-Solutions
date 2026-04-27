import numpy as np

def top_k_recommendations(scores, rated_indices, k):
    scores = np.array(scores, dtype=float)
    rated_indices = np.array(list(rated_indices))
    if len(rated_indices) != 0 :
        scores[rated_indices] = -np.inf
    siz = min(len(scores) - len(rated_indices), k)
    top_k_indices = np.lexsort((-np.arange(len(scores)), scores))[-siz:][::-1]
    indices = np.lexsort((-top_k_indices, scores[top_k_indices]))[::-1]
    return top_k_indices[indices].tolist()
  