###########################
#### Exercise Function ####
###########################
def get_orthographic_projection(x_c):
    ''' Projects the 3D point in camera space x_c to 2D pixel coordinates using an orthographic projection.

    Args:
        x_c (array): 3D point in camera space
    '''
    assert (x_c.shape == (3,))

    # Insert your code here
    x_s = np.array([x_c[0], x_c[1]], dtype=np.float32)
    assert (x_s.shape == (2,))
    return x_s