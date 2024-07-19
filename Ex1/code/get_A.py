###########################
#### Exercise Function ####
###########################
def get_A(points_source, points_target):
    ''' Returns the A matrix discussed in the lecture.

    Args:
        points_source (array): 3D homogeneous points from source image
        points_target (array): 3D homogeneous points from target image
    '''
    N = points_source.shape[0]

    # Insert your code here
    for i in range(N):
        xi_vector = points_source[i]
        xi_prime_vector = points_target[i]
        Ai = get_Ai(xi_vector, xi_prime_vector)
        if i == 0:
            A = Ai
        else:
            A = np.vstack([A, Ai])

    assert (A.shape == (2 * N, 9))
    return A