###########################
#### Exercise Function ####
###########################
import numpy as np


def get_face_color(normal, point_light_direction=(0, 0, 1)):
    ''' Returns the face color for input normal.

    Args:
        normal (array): 3D normal vector
        point_light_direction (tuple): 3D point light direction vector
    '''
    assert (normal.shape == (3,))
    point_light_direction = np.array(point_light_direction, dtype=np.float32)

    # Insert your code here
    L_in = 1
    BRDF = 1
    dot_product = np.dot(normal, point_light_direction)
    norm_normal = np.linalg.norm(normal)
    norm_direction = np.linalg.norm(point_light_direction)
    cos_angle = abs(dot_product/(norm_normal*norm_direction))
    light_intensity = L_in*BRDF*cos_angle
    color_intensity = 0.1 + (light_intensity * 0.5 + 0.5) * 0.8
    color = np.stack([color_intensity for i in range(3)])
    return color