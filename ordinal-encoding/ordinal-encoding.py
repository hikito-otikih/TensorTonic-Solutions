def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    ans = []
    for value in values :
        for i, order in enumerate(ordering) :
            if order == value :
                ans.append(i)
                break
    return ans
            