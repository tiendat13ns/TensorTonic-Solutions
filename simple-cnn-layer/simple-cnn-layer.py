import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    N, C_in, H, W_in = x.shape
    C_out, _, KH, KW = W.shape

    H_out = H - KH + 1
    W_out = W_in - KW + 1

    out = np.zeros((N, C_out, H_out, W_out))

    for n in range(N):
        for cout in range(C_out):
            for i in range(H_out):
                for j in range(W_out):
                    s = 0
                    for cin in range(C_in):
                        patch = x[n, cin, i:i+KH, j:j+KW]
                        s += np.sum(patch * W[cout, cin])
                    out[n, cout, i, j] = s + b[cout]

    return out
    pass