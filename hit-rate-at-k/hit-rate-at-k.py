def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hrak = 0
    for i in range(len(recommendations)) :
        recom = recommendations[i]
        for gr in ground_truth[i] :
            if gr in recom[:k] :
                hrak += 1

    return 1.0 / len(recommendations) * hrak