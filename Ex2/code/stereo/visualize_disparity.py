###########################
#### Exercise Function ####
###########################

def visualize_disparity(disparity, im_left, im_right, title='Disparity Map', max_disparity=50):
    """
    Generates a visualization for the disparity map.

    Args:
        disparity (np.array): disparity map
        title: plot title
        out_file: output file path
        max_disparity: maximum disparity
    """
    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 2)
    # visualize stereo pair
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    plt.title(title)
    plt.axis('off')

    ax1.imshow(im_left)

    ax2.imshow(disparity, cmap='Spectral', vmin=0, vmax=max_disparity)

    plt.tight_layout()
    plt.show()
    # -------------------------------------