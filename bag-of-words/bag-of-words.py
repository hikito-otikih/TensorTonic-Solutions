import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    dict = {}
    for voc in vocab :
        dict[voc] = 0
    for token in tokens :
        if token in vocab :
            dict[token] += 1
    return np.array(list(dict.values())).astype(int)