def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here
    ans = []
    for r, v in items :
        ans.append(1.0 * v / (v + min_votes) * r + 1.0 * min_votes / (v + min_votes) * global_mean)
    return ans