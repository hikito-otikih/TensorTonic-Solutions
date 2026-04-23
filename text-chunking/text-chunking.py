def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    ans = []
    for i in range(0, len(tokens), chunk_size - overlap) :
        if i + chunk_size > len(tokens) and i > 0:
            break 
        res = []
        for j in range(i, min(i + chunk_size, len(tokens))) :
            res.append(tokens[j])
        ans.append(res)
    return ans