def promote_model(models):
    """
    Decide which model version to promote to production.
    """
    # Write code here
    bmodel = None
    for model in models :
        if bmodel == None :
            bmodel = model
        else :
            if model["accuracy"] > bmodel["accuracy"] :
                bmodel = model
            elif model["accuracy"] == bmodel["accuracy"] :
                if model["latency"] < bmodel["latency"] :
                    bmodel = model
                elif model["latency"] == bmodel["latency"] :
                    if model["timestamp"] > bmodel["timestamp"] :
                        bmodel = model
    return bmodel["name"]