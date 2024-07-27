###########################
#### Exercise Function ####
###########################
def compute_fundamental_matrix(keypoints1, keypoints2):
    '''
    Computes the fundamental matrix from image coordinates using the 8-point
    algorithm by constructing and solving the corresponding linear system.

    Args:
        keypoints1 (np.ndarray): Nx3 array of correspondence points in first
            view in homogenous image coordinates.
        keypoints2 (np.ndarray): Nx3 array of correspondence points in second
            view in homogenous image coordinates.

    Returns:
        F (np.ndarray): 3x3 fundamental matrix.
    '''
    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 1)
    # -------------------------------------

    for i in range(keypoints1.shape[0]):
        x_vector = keypoints1[i]
        x, y, w = keypoints2[i]
        if i == 0:
            A = np.array([x * x_vector, y * x_vector, w * x_vector]).reshape(1, 9)
        else:
            A = np.vstack((A, np.array([x * x_vector, y * x_vector, w * x_vector]).reshape(1, 9)))
    U, S, V = np.linalg.svd(A)
    F = V[-1].reshape(3, 3)
    U, S, V = np.linalg.svd(F)
    S[2] = 0
    F = U @ np.diag(S) @ V
    F = F / F[2, 2]
    return F

