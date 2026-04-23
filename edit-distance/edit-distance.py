import numpy as np
def edit_distance(s1, s2):
    """
    Compute the minimum edit distance between two strings.
    """
    dp = np.full((len(s1) + 1, len(s2) + 1), 1000000)
    dp[0][0] = 0
    for i in range(len(s1)) :
        dp[i + 1][0] = i + 1
    for i in range(len(s2)) :
        dp[0][i + 1] = i + 1
    for i, s in enumerate(s1) : 
        for j, x in enumerate(s2) :
            dp[i + 1][j + 1] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i][j])
            if s == x :
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
    return int(dp[len(s1)][len(s2)])
    