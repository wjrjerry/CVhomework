###########################
#### Exercise Function ####
###########################
# Insert your code here
K_list = [get_camera_intrinsics(fx=f,fy=f) for f in np.linspace(10, 150, 30)]
cube_list = [get_cube(rotation_angles=(0, 30, 50), with_normals=True) for i in range(30)]
anim = get_animation(K_list, cube_list, title="Change of focal length along the x-axis and y-axis.")
HTML(anim.to_html5_video())