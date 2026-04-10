def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    ret = 1
    ans = []
    for re in returns :
        ret *= (1 + re)
        ans.append(ret - 1)
    return ans
        