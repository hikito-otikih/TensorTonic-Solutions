import numpy as np
def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    series = np.array(series).astype(float)
    top = np.delete(series, 0)
    down = np.delete(series, -1)
    return np.where(down == 0, 0, (top - down) / down)
    