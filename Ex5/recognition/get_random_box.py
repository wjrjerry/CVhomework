###########################
#### Exercise Function ####
###########################
def get_random_box(boxsize, imsize):
  """ Returns randomly located box with same size as box. 
  
  Args:
  boxsize (tuple): width, height of box
  imsize (tuple): width, height of image / image boundaries
  """
  W, H = imsize
  
  # 随机的box作为负面样例
  # Insert your code here
  box_width, box_height = boxsize
  img_width, img_height = imsize
  
  x_min = random.randint(0, img_width - box_width - 1)
  y_min = random.randint(0, img_height - box_height - 1)

  x_max = x_min + box_width
  y_max = y_min + box_height
  
  box = (x_min, y_min, x_max, y_max)
  
  assert all(b >= 0 for b in box) and (box[2] < W) and (box[3] < H), f'Box {box} out of image bounds {W, H}.'
  return box