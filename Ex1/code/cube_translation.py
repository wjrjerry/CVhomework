###########################
#### Exercise Function ####
###########################
# Insert your code here
K_list = [get_camera_intrinsics() for i in range(30)]
cube_list = [get_cube(center=(0, y, 2), with_normals=True) for y in np.linspace(-2,2,30)]
anim = get_animation(K_list, cube_list, title="Translation along the y-axis.")
HTML(anim.to_html5_video())