###########################
#### Exercise Function ####
###########################
def add_offset_to_box(box, imsize):
  """ Add a small random integer offset to the box.

  Args:
  box (iterable): (left, upper, right, lower) pixel coordinate
  imsize (tuple): width, height of image / image boundaries
  """
  W, H = imsize

  # Insert your code 
  off_box = np.zeros(4, dtype=int)
  off_box[0] = box[0] + random.randint(1, int(0.2 * (box[2] - box[0]))) * random.choice([-1, 1])
  off_box[1] = box[1] + random.randint(1, int(0.2 * (box[3] - box[1]))) * random.choice([-1, 1])
  off_box[2] = box[2] - box[0] + off_box[0]
  off_box[3] = box[3] - box[1] + off_box[1]

  # ensure to stay within image boundaries / do not mind changing size slightly
  off_box[0] = max(0, off_box[0])
  off_box[1] = max(0, off_box[1])
  off_box[2] = min(W-1, off_box[2])  
  off_box[3] = min(H-1, off_box[3])

  assert all(b >= 0 for b in off_box) and (off_box[2] < W) and (off_box[3] < H), f'Box {off_box} out of image bounds {W, H}.'

  return off_box