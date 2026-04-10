def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    while order > 0 :
        order -= 1
        for i in reversed(range(1, len(series))) :
            series[i] -= series[i - 1]
        series.pop(0)
    return series