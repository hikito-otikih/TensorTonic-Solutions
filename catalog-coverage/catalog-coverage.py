import numpy as np
def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    rec = np.array([])
    for reccom in recommendations :
        rec = np.concatenate((rec, np.array(reccom)), axis=0)
        print(rec)
    
    return 1.0 * np.unique(rec).size / n_items