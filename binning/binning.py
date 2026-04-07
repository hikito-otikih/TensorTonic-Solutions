import numpy as np
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    values = np.array(values)
    w = (values.max() - values.min()) / num_bins
    if w == 0:
        return [0] * values.size
        
    min_x = values.min()
    bin = (values - min_x) // w
    nb = np.full(values.size, num_bins - 1)
    
    bin = np.stack((bin, nb), axis=0)
    return bin.min(axis=0).tolist()