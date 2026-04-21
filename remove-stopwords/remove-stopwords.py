def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    new_tokens = []

    for token in tokens :
        if not (token in stopwords) :
            new_tokens.append(token)
    return new_tokens