def relight_scene(light_pos, normals_unit, albedo, mask):
    """
    light_pos np.array [k,3] np.float32 注释给的不对，只有一个光源
    mask np.array [h,w] np.bool
    ----
    dims:
    h: image height (num rows)
    w: image width (num cols)
    ----
    returns:
        imgs np.array [h,w] np.float32 [0.0, 1.0]
    """
    assert light_pos.shape == (3,)
    assert np.allclose(1.0, np.linalg.norm(light_pos))
    assert normals_unit.shape[-1] == 3
    k = light_pos.shape[0]
    # print(k)
    h, w = mask.shape
    assert len(normals_unit.shape) == 3
    img = np.zeros((h, w), dtype=np.float32)

    # BEGIN REGION SOLUTION
    for row in range(h):
        for col in range(w):
            if mask[row, col]:
                img[row, col] = np.dot(normals_unit[row, col], light_pos) * albedo[row,col] #输入的可以是数组或者是数
            else:
                img[row, col] = 0
                    
    img_norm = (img - img.min()) / (img.max() - img.min())
    img_norm = np.where(mask, img_norm, np.zeros_like(albedo))
    

    # END REGION SOLUTION
    assert np.all(
        np.logical_and(0.0 <= img_norm, img_norm <= 1.0)
    ), "please normalize your image to interval [0.0,1.0]"
    return img_norm.reshape(h,w)


# 下面的block修改后的代码
light_pos = np.array([0.5, 0.5, 0.7])
new_albedo = 0.5
for x in np.linspace(-2, 2, 5):
    light_pos[0] = x
    light_pos = np.array(light_pos / np.linalg.norm(light_pos))

    # new_img = relight_scene(light_pos, normals_unit, new_albedo, mask)
    new_img = relight_scene(light_pos, normals_unit, rho, mask)
    plt.figure()
    plt.imshow(new_img, cmap=plt.cm.gray)
    plt.title(
        "Relit image \nNew light position @ {0}\nAlbedo is now {1}".format(light_pos, new_albedo)
        )
    plt.show()