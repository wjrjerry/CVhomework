def compute_normals_albedo_map(imgs, mask, light_positions):
    """
    imgs np.array [k,h,w] np.float32 [0.0, 1.0]
    mask np.array [h,w] np.bool
    light_positions np.array [k,3] np.float32
    ---
    dims:
    k: number of images
    h: image height (num rows)
    w: image width (num cols)
    """
    # BEGIN REGION SOLUTION
    k, h, w = imgs.shape
    normals_unit = np.zeros((h, w, 3), dtype=np.float32)
    rho = np.zeros((h, w), dtype=np.float32)
    for row in range(h):
        for col in range(w):
            if mask[row, col]:
                normals_unit[row, col] = np.linalg.lstsq(light_positions, imgs[:, row, col], rcond=None)[0] #p n(T)@s=R
                norm = np.linalg.norm(normals_unit[row, col])
                if norm > 0:
                    normals_unit[row, col] /= norm
                rho[row, col] = norm
            else:
                normals_unit[row, col] = np.array([0, 0, 0])
                rho[row, col] = 0
                
    # END REGION SOLUTION

    assert normals_unit.shape == (imgs.shape[1], imgs.shape[2], 3)
    assert rho.shape == (imgs.shape[1], imgs.shape[2])

    rho = np.clip(rho,0.0,1.0)
    normals_unit = np.clip(normals_unit, 0.0, 1.0)

    return normals_unit, rho, mask