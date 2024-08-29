###########################
##### Helper Function #####
###########################
def add_padding(I, padding):
    """
    Adds zero padding to an RGB or grayscale image.

    Args:
        I (np.ndarray): HxWx? numpy array containing RGB or grayscale image

    Returns:
        P (np.ndarray): (H+2*padding)x(W+2*padding)x? numpy array containing zero padded image
    """
    if len(I.shape) == 2:
        H, W = I.shape
        padded = np.zeros((H + 2 * padding, W + 2 * padding), dtype=np.float32)
        padded[padding:-padding, padding:-padding] = I
    else:
        H, W, C = I.shape
        padded = np.zeros((H + 2 * padding, W + 2 * padding, C), dtype=I.dtype)
        padded[padding:-padding, padding:-padding] = I

    return padded


###########################
#### Exercise Function ####
###########################
def sad(image_left, image_right, window_size=3, max_disparity=50):
    """
    Compute the sum of absolute differences between image_left and image_right.

    Args:
        image_left (np.ndarray): HxW numpy array containing grayscale right image
        image_right (np.ndarray): HxW numpy array containing grayscale left image
        window_size: window size (default 3)
        max_disparity: maximal disparity to reduce search range (default 50)

    Returns:
        D (np.ndarray): HxW numpy array containing the disparity for each pixel
    """

    D = np.zeros_like(image_left)

    # add zero padding
    padding = window_size // 2
    image_left = add_padding(image_left, padding).astype(np.float32)
    image_right = add_padding(image_right, padding).astype(np.float32)

    height = image_left.shape[0]
    width = image_left.shape[1]

    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 1)
    # -------------------------------------
    for i in range(height - window_size + 1):
        for j in range(width - window_size + 1):
            cost = []
            for d in range(max_disparity + 1):
                if j - d >= 0:
                    patch_left = image_left[i:i + window_size, j:j + window_size]
                    patch_right = image_right[i:i + window_size, j - d:j + window_size - d]
                    diff = np.sum(np.abs(patch_left - patch_right))
                    cost.append(diff)
            D[i, j] = np.argmin(cost)

    return D


###########################
##### Bonus Function #####
###########################
def sad_convolve(image_left, image_right, window_size=3, max_disparity=50):
    """
    Compute the sum of absolute differences between image_left and image_right
    by using a mean filter.

    Args:
        image_left (np.nfarray): HxW numpy array containing grayscale right image
        image_right (np.nfarray): HxW numpy array containing grayscale left image
        window_size: window size (default 3)
        max_disparity: maximal disparity to reduce search range (default 50)

    Returns:
        D (np.ndarray): HxW numpy array containing the disparity for each pixel
    """
    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 1 BONUS)
    # -------------------------------------
    height, width = image_left.shape
    kernel = np.ones((window_size, window_size)) / window_size ** 2
    pD = np.zeros((height, width, max_disparity + 1))

    for d in range(max_disparity + 1):
        image_right_shift = np.zeros((height, width))
        image_right_shift[:, d:width] = image_right[:, :width - d]
        image_diff = np.abs(image_right_shift - image_left)
        image_filter = convolve(image_diff, kernel, mode='same')
        pD[:, :, d] = image_filter

    D = np.argmin(pD, axis=2)
    return D
