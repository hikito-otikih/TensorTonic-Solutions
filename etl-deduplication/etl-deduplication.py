def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    deduped = {}
    
    for record in records:
        comp_key = tuple(record[k] for k in key_columns)
        
        if comp_key not in deduped:
            deduped[comp_key] = record
        else:
            if strategy == "first":
                pass 
                
            elif strategy == "last":
                deduped[comp_key] = record 
                
            elif strategy == "most_complete":
                current_best = deduped[comp_key]
                current_nones = sum(1 for v in current_best.values() if v is None)
                new_nones = sum(1 for v in record.values() if v is None)
                
                if new_nones < current_nones:
                    deduped[comp_key] = record

    return list(deduped.values())