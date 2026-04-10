import numpy as np

def compute_advantage(states, rewards, V, gamma):
    """
    Returns: A (NumPy array of advantages)
    """
    # Write code here
    states = np.array(states)
    rewards = np.array(rewards).astype(float)
    V = np.array(V).astype(float)
    cur_reward = 0
    A = []
    for i in reversed(range(rewards.size)) :
        cur_reward = rewards[i] + gamma * cur_reward
        A.append(cur_reward  - V[states[i]])
    A.reverse()
    return A
