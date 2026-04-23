def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    dict = {}

    for value in values :
        if not(value in dict) :
            dict[value] = 1
        else :
            dict[value] += 1
    ans = []
    for value in values :
        ans.append(dict[value] * 1.0 / len(values))
    return ans