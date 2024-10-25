def create_artificial_sphere_sdf(voxel_coordinates, radius):
    voxel_dist_to_center = np.linalg.norm(voxel_coordinates, axis=-1, keepdims=True)
    # 是一个三维tensor

    # lets have a sdf, where at center of sphere sdf = 1, at border = 0, linear
    
    # BEGIN REGION SOLUTION
    sdf_vals = radius - voxel_dist_to_center

    # END REGION SOLUTION

    assert sdf_vals.shape[:-1] == voxel_coordinates.shape[:-1]
    assert sdf_vals.shape[-1] == 1
    return sdf_vals