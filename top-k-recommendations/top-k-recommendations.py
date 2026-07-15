def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    rated = set(rated_indices)

    candidates = [
        (idx, score)
        for idx, score in enumerate(scores)
        if idx not in rated
    ]

    candidates.sort(key=lambda x: x[1], reverse=True)

    return [idx for idx, _ in candidates[:k]]