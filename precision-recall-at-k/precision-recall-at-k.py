def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    count = 0
    for i in range(k) :
        for j in relevant :
            if recommended[i] == j :
                count += 1
    return [count / k, count / len(relevant)]