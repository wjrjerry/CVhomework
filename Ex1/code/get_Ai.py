###########################
#### Exercise Function ####
###########################
def get_Ai(xi_vector, xi_prime_vector):
    ''' Returns the A_i matrix discussed in the lecture for input vectors.

    Args:
        xi_vector (array): the x_i vector in homogeneous coordinates
        xi_vector_prime (array): the x_i_prime vector in homogeneous coordinates
    '''
    assert (xi_vector.shape == (3,) and xi_prime_vector.shape == (3,))

    # Insert your code here

    Ai = np.array([
        [0, 0, 0, -xi_prime_vector[2] * xi_vector[0], -xi_prime_vector[2] * xi_vector[1],
         -xi_prime_vector[2] * xi_vector[2], xi_prime_vector[1] * xi_vector[0], xi_prime_vector[1] * xi_vector[1],
         xi_prime_vector[1] * xi_vector[2]],
        [xi_prime_vector[2] * xi_vector[0], xi_prime_vector[2] * xi_vector[1], xi_prime_vector[2] * xi_vector[2], 0, 0,
         0, -xi_prime_vector[0] * xi_vector[0], -xi_prime_vector[0] * xi_vector[1], -xi_prime_vector[0] * xi_vector[2]]
    ])

    assert (Ai.shape == (2, 9))
    return Ai