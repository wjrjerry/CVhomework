
def random_points_on_sphere(radius, num_points, center=np.array([0.0, 0.0, 0.0])):

    # BEGIN REGION SOLUTION
    phi = np.random.rand(num_points) * 2 * np.pi
    theta = np.random.rand(num_points) * np.pi
    x = radius * np.cos(theta) * np.sin(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(phi)
    points = np.stack([x,y,z],axis=-1)+center
    # END REGION SOLUTION

    assert points.shape == (num_points, 3)
    return points
