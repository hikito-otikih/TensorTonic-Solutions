import numpy as np
def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    paras = np.array([[[0.299, 0.587, 0.114]]])
    
    return np.sum(np.array(image).astype(float) * paras, axis=2).tolist()
    
    