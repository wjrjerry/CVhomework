###########################
#### Exercise Function ####
###########################
def compute_fundamental_matrix_normalized(keypoints1, keypoints2):
    '''
    Computes the fundamental matrix from image coordinates using the normalized
    8-point algorithm by first normalizing the keypoint coordinates to zero-mean
    and unit variance, then constructing and solving the corresponding linear
    system and finally undoing the normaliziation by back-transforming the
    resulting matrix.

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
    # TODO: ENTER CODE HERE (EXERCISE 2)
    # -------------------------------------
    s1_mean = np.mean(keypoints1, axis=0)
    s2_mean = np.mean(keypoints2, axis=0)

    s1_scale = np.sqrt(2) / np.mean(np.linalg.norm(keypoints1 - s1_mean, axis=1))
    s2_scale = np.sqrt(2) / np.mean(np.linalg.norm(keypoints2 - s2_mean, axis=1))

    T1 = np.array([[s1_scale, 0, -s1_scale * s1_mean[0]], [0, s1_scale, -s1_scale * s1_mean[1]], [0, 0, 1]])
    T2 = np.array([[s2_scale, 0, -s2_scale * s2_mean[0]], [0, s2_scale, -s2_scale * s2_mean[1]], [0, 0, 1]])

    keypoints1_normalized = (T1 @ keypoints1.T).T
    keypoints2_normalized = (T2 @ keypoints2.T).T

    F = compute_fundamental_matrix(keypoints1_normalized, keypoints2_normalized)

    F = T2.T @ F @ T1
    F = F / F[2, 2]

    return F