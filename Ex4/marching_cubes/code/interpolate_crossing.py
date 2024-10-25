def interpolate_crossing(loc_x1, sdf_val_at_x1, loc_x2, sdf_val_at_x2, thresh=0.0):
    # avoid divison by zero
    if sdf_val_at_x1 == sdf_val_at_x2:
        crossing_location = (loc_x2 + loc_x1) / 2
    else:
    # BEGIN REGION SOLUTION
    # interpolate here
    
        t = (thresh - sdf_val_at_x1) / (sdf_val_at_x2 - sdf_val_at_x1)
        crossing_location = loc_x1 + t * (loc_x2 - loc_x1)
    # END REGION SOLUTION
        
    return crossing_location
