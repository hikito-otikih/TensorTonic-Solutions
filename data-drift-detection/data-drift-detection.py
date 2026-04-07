import numpy as np
def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    reference_counts = np.array(reference_counts) * 1.0
    production_counts = np.array(production_counts) * 1.0
    reference_counts /= reference_counts.sum()
    production_counts /= production_counts.sum()
    score = np.sum(np.abs(reference_counts - production_counts)) * 0.5
    return {"score":score, "drift_detected" : bool(score > threshold)}
    