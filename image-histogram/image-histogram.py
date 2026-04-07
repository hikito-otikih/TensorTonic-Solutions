import numpy as np
def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    img_array = np.array(image).ravel()
    hist = np.bincount(img_array, minlength=256)
    return hist.tolist()