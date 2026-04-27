import numpy as np
def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    dict = {}
    for i, category in enumerate(categories) :
        if not (category in dict) :
            dict[category] = np.array([targets[i], 1])
        else :
            dict[category] += np.array([targets[i], 1])
    ans = []
    for category in categories :
        value = dict[category]
        ans.append(1.0 * value[0] / value[1])
    return ans