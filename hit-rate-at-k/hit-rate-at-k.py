def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    hits = 0

    for recs, truth in zip(recommendations, ground_truth):
        top_k = recs[:k]
        truth_set = set(truth)

        # Count as a hit if at least one relevant item is in the top-K recommendations
        if any(item in truth_set for item in top_k):
            hits += 1

    return hits / len(recommendations)

