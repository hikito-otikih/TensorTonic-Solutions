def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x_left = max(box_a[0], box_b[0])
    y_left = max(box_a[1], box_b[1])
    x_right = min(box_a[2], box_b[2])
    y_right = min(box_a[3], box_b[3])
    intersec = max(0, x_right - x_left) * max(0, y_right - y_left) * 1.0
    area_a = (box_a[2] - box_a[0]) * (box_a[3] - box_a[1]) * 1.0
    area_b = (box_b[2] - box_b[0]) * (box_b[3] - box_b[1]) * 1.0
    return intersec / (area_a + area_b - intersec)