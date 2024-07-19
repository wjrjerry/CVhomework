import numpy as np


def get_perspective_projection(x_c, K):
    ''' Projects the 3D point x_c to screen space and returns the 2D pixel coordinates.

    Args:
        x_c (array): 3D point in camera space
        K (array): camera intrinsics matrix (3x3)
    '''
    assert (x_c.shape == (3,) and K.shape == (3, 3))

    # Insert your code here
    x_s_homo = np.matmul(K, x_c)
    w = x_s_homo[2]
    x_s = np.array([x_s_homo[0]/w, x_s_homo[1]/w], dtype=np.float32)


    return x_s