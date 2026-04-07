import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    V = np.zeros(n_states)
    init_state = np.zeros(n_states)
    
    for episode in episodes :
        episode = np.array(episode)
        state = episode[:,0].astype(int)
        reward = episode[:,1].astype(float)
        R = 0
        for i in reversed(range(reward.size)) :
            R = R * gamma + reward[i]
            reward[i] = R

        uni_state, first_idx = np.unique(state, return_index=True)
        V[uni_state] += reward[first_idx]
        init_state[uni_state] += 1
        
    idx = np.where(init_state > 0)
    V[idx] = V[idx] / init_state[idx]
    return V
