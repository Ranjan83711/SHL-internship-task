def precision_at_k(retrieved, relevant, k):
    """
    Precision@K with partial & case-insensitive matching
    """
    retrieved_k = retrieved[:k]
    relevant_lower = [r.lower() for r in relevant]

    hits = 0
    for item in retrieved_k:
        item_lower = item.lower()
        if any(rel in item_lower or item_lower in rel for rel in relevant_lower):
            hits += 1

    return hits / k


def hit_rate_at_k(retrieved, relevant, k):
    """
    HitRate@K with partial & case-insensitive matching
    """
    retrieved_k = retrieved[:k]
    relevant_lower = [r.lower() for r in relevant]

    for item in retrieved_k:
        item_lower = item.lower()
        if any(rel in item_lower or item_lower in rel for rel in relevant_lower):
            return 1

    return 0
