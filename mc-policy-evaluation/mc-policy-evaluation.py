import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    V = np.zeros(n_states)
    init_state = np.zeros(n_states)
    check_in_episodes = np.zeros(n_states)
    po = np.power(gamma, np.arange(0, 500))
    for episode in episodes :
        episode = np.array(episode)
        reward = episode[:,1] * 1.0
        visited_list = []
        for i in range(reward.size):
            if check_in_episodes[episode[i, 0]] == 0 :
                V[episode[i, 0]] += reward[i:].dot(po[:reward.size - i])
                check_in_episodes[episode[i, 0]] = 1
                init_state[episode[i, 0]] += 1
                visited_list.append(episode[i, 0])
        for x in visited_list:
            check_in_episodes[x] = 0
    idx = np.where(init_state > 0)
    V[idx] = V[idx] / init_state[idx]
    return V
