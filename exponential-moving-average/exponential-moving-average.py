def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    ema = []
    for i, value in enumerate(values) :
        if i == 0 :
            ema.append(value)
        else :
            ema.append(alpha * value + (1 - alpha) * ema[i - 1])
    return ema