import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.empty((0, max_len or 0))

    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)
    N = len(seqs)
    result = np.full((N, max_len), pad_value)
    for i, seq in enumerate(seqs):
        cols_to_copy = min(len(seq), max_len)
        if cols_to_copy > 0: 
            result[i, :cols_to_copy] = seq[:cols_to_copy]

    return result