###########################
#### Exercise Function ####
###########################
# Insert your code here
K_list = [get_camera_intrinsics(fx=f,fy=f) for f in np.linspace(10, 150, 30)]
cube_list = [get_cube(center=(0, 0, z),rotation_angles=(30, 50, 0), with_normals=True) for z in np.linspace(0.9,5,30)]
anim = get_animation(K_list, cube_list, title="Dolly zoom effect.")
HTML(anim.to_html5_video())