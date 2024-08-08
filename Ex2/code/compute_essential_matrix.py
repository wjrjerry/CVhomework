###########################
#### Exercise Function ####
###########################
def compute_essential_matrix(F, K1, K2):
    '''
    Computes the essential from the fundamental matrix given known intrinsics.

    Args:
        F (np.ndarray): 3x3 fundamental matrix.
        K1 (np.ndarray): The 3x3 calibration matrix K for the first
            view/camera.
        K2 (np.ndarray): The 3x3 calibration matrix K for the second
            view/camera.

    Returns:
        E (np.ndarray): 3x3 essential matrix.
    '''
    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 3)
    # -------------------------------------

    E = K2.T @ F @ K1

    return E