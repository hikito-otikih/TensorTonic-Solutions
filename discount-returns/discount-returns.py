def discount_returns(rewards, gamma):
    """
    Compute the discounted return at every timestep.
    """
    # Write code here
    N = len(rewards)
    for i in range(N) :
        if i == 0 :
        	continue
        rewards[N - i - 1] += rewards[N - i] * gamma
    return rewards  