def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    deduped = {}
    
    for record in records:
        # 1. Tạo Composite Key bằng Tuple (bắt buộc phải là tuple mới dùng làm key cho dict được)
        # Ví dụ: comp_key = ("2024-01-01", 1)
        comp_key = tuple(record[k] for k in key_columns)
        
        # 2. Xử lý lưu trữ
        if comp_key not in deduped:
            # Lần đầu tiên nhìn thấy khóa này -> Luôn luôn lưu lại
            deduped[comp_key] = record
        else:
            # Nếu khóa đã tồn tại, áp dụng chiến lược để quyết định có ghi đè hay không
            if strategy == "first":
                pass # Giữ nguyên cái đầu tiên, không làm gì cả
                
            elif strategy == "last":
                deduped[comp_key] = record # Ghi đè bằng record mới nhất
                
            elif strategy == "most_complete":
                # Đếm số lượng None của record đang lưu (best) và record mới (new)
                current_best = deduped[comp_key]
                current_nones = sum(1 for v in current_best.values() if v is None)
                new_nones = sum(1 for v in record.values() if v is None)
                
                # Chỉ ghi đè nếu record mới ít None hơn.
                # (Vì nếu bằng nhau, đề bài yêu cầu giữ nguyên occurrence đầu tiên)
                if new_nones < current_nones:
                    deduped[comp_key] = record

    # 3. Trả về kết quả
    # Vì Python Dict giữ nguyên thứ tự thêm vào lần đầu tiên của các keys, 
    # nên list(deduped.values()) tự động thỏa mãn yêu cầu "Preserve Order" cực kỳ hoàn hảo!
    return list(deduped.values())