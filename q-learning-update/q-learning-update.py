import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q = np.array(Q).astype(float)
    maxQ = np.max(Q[s_next])
    reward = r + gamma * maxQ
    Q[s][a] += alpha * (reward - Q[s][a])
    return Q