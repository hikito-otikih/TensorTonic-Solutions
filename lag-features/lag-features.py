def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    # get max
    max_lags = lags[0]
    for lag in lags :
        max_lags = max(max_lags, lag)
    ans = []
    for x in range(max_lags, len(series)) :
        res = []
        for y in lags:
            res.append(series[x - y])
        ans.append(res)
    return ans