def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    answer = []
    for request in requests :
        id = request["user_id"]
        if not(id in feature_store) :
            answer.append(request["online_features"] | defaults)
        else :
            answer.append(request["online_features"] | feature_store[id])
    return answer
            