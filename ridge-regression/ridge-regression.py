def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    n_features = X.shape[1]
    I = np.eye(n_features)

    w = np.linalg.inv(X.T @ X + lam * I) @ X.T @ y

    return w