###########################
#### Exercise Function ####
###########################
def get_homography(points_source, points_target):
    ''' Returns the homography H.

    Args:
        points_source (array): 3D homogeneous points from source image
        points_target (array): 3D homogeneous points from target image
    '''

    # Insert your code here
    U, Sigma, Vt = np.linalg.svd(get_A(points_source, points_target))
    H = Vt[-1].reshape(3, 3)

    assert (H.shape == (3, 3))
    return H