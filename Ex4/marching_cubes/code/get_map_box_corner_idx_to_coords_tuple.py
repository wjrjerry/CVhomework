def get_map_box_corner_idx_to_coords_tuple(x_idx, y_idx, z_idx): 
    map_box_corner_idx_to_coords_tuple = {
        0: (x_idx, y_idx, z_idx),
        1: (x_idx, y_idx + 1, z_idx),
        # BEGIN REGION SOLUTION: fill in the missing cases
        # 将顶点的编号映射到坐标
        2: (x_idx + 1, y_idx + 1, z_idx),
        3: (x_idx + 1, y_idx, z_idx),
        4: (x_idx, y_idx, z_idx + 1),
        5: (x_idx, y_idx + 1, z_idx + 1),
        6: (x_idx + 1, y_idx + 1, z_idx + 1),
        7: (x_idx + 1, y_idx, z_idx + 1),
        # END REGION SOLUTION
    }

    assert len(map_box_corner_idx_to_coords_tuple) == 8, "you missed some cases or added too many"
    return map_box_corner_idx_to_coords_tuple