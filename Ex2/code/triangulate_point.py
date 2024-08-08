# From the essential matrix we can recover the relative rotation and
# translation between views
E = compute_essential_matrix(F_normalized, K1, K2)
R1, R2, t = cv2.decomposeEssentialMat(E)


###########################
##### Helper Function #####
###########################
def assemble_pose_matrix(R, t):
    '''
    Builds 4x4 pose matrix (extrinsics) from 3x3 rotation matrix and
    3-d translation vector. See also lecture two.

    Args:
        R (np.ndarray): 3x3 rotation matrix.
        t (np.ndarray): 3-d translation vector.

    Returns:
        pose (np.ndarray): 4x4 pose matrix (extrinsics).
    '''
    # augment R
    R = np.concatenate([R, np.zeros([1, 3])], axis=0)

    # augment T
    t = np.concatenate([t, np.ones([1, 1])])

    # assemble and return pose matrix
    return np.concatenate([R, t], axis=1)


###########################
##### Helper Function #####
###########################
def assemble_projection_matrix(K, R, t):
    '''
    Builds 3x4 projection matrix from 3x3, calibration matrix, 3x3 rotation
    matrix and 3-d translation vector. See also lecture two.

    Args:
        K (np.ndarray): 3x3 calibration matrix.
        R (np.ndarray): 3x3 rotation matrix.
        t (np.ndarray): 3-d translation vector.

    Returns:
        P (np.ndarray): 4x4 pose matrix.
    '''
    # TODO: use assemble pose
    # augment K
    K = np.concatenate([K, np.zeros([3, 1])], axis=1)

    # augment R
    R = np.concatenate([R, np.zeros([1, 3])], axis=0)

    # augment T
    t = np.concatenate([t, np.ones([1, 1])])

    # assemble and return camera matrix P
    return K @ np.concatenate([R, t], axis=1)


###########################
#### Exercise Function ####
###########################
def triangulate_point(keypoint1, keypoint2, K1, K2, R, t):
    '''
    Triangulates world coordinates given correspondences from two views with
    relative extrinsics R and t.

    Args:
        keypoints1 (np.ndarray): Nx3 array of correspondence points in first
            view in homogenous image coordinates.
        keypoints2 (np.ndarray): Nx3 array of correspondence points in second
            view in homogenous image coordinates.
        K1 (np.ndarray): The 3x3 calibration matrix K for the first
            view/camera.
        K2 (np.ndarray): The 3x3 calibration matrix K for the second
            view/camera.
        R (np.ndarray): 3x3 rotation matrix from first to second view.
        t (np.ndarray): 3-d translation vector from first to second view.

    Returns:
        x_w (np.ndarray): Nx4 array of 3-d points in homogenous world
            coordinates.
    '''
    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 4)
    # -------------------------------------
    P1 = assemble_projection_matrix(K1, np.eye(3), np.zeros([3, 1]))
    P2 = assemble_projection_matrix(K2, R, t)

    A = np.array([keypoint1[0] * P1[2] - P1[0],
                  keypoint1[1] * P1[2] - P1[1],
                  keypoint2[0] * P2[2] - P2[0],
                  keypoint2[1] * P2[2] - P2[1]])
    U, S, V = np.linalg.svd(A)
    x_w = V[-1]
    x_w = x_w / x_w[3]

    return x_w