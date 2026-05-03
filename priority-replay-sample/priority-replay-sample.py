import numpy as np
def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    # Write code here
    priorities = np.array(priorities)
    priorities = priorities ** alpha
    Pros = priorities / np.sum(priorities)
    weights = (len(priorities) * Pros) ** (-beta)

    return [Pros.tolist(), (weights / np.max(weights)).tolist()]