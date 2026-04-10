def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = list(set(set_a))
    set_b = list(set(set_b))

    idx_a = 0
    idx_b = 0

    inter_count = 0
    while idx_a < len(set_a) and idx_b < len(set_b) :
        if set_a[idx_a] == set_b[idx_b] :
            inter_count += 1
            idx_a += 1
            idx_b += 1
        elif set_a[idx_a] <= set_b[idx_b] : 
            idx_a += 1
        else :
            idx_b += 1
    population = len(set_a) + len(set_b) - inter_count
    if population == 0 :
        return 0.0
    return inter_count * 1.0 / population