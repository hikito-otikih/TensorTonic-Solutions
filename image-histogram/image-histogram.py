def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    colors = [0] * 256
    for x in image:
        for y in x:
            colors[y] += 1
    return colors