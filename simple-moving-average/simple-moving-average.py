def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    ans = []
    curS = 0.0
    for i in range(window_size - 1) :
        curS += values[i]
    for i in range(window_size - 1, len(values)) :
        curS += values[i]
        ans.append(curS / window_size)
        curS -= values[i - window_size + 1]
    return ans