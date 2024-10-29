###########################
#### Exercise Function ####
###########################
def img_to_hog_patches(img, window_size, patch_size, step_size=1):
  """ Extract hog feature patches from an image using a sliding window approach.

  Args:
  img (PIL.Image.Image): image
  window_size (tuple): width, height of window
  patch_size (tuple): width, height of resized patch
  step_size (int): step size of window (for faster evaluation)
  """
  
  # Insert your code here

  img_height, img_width = np.array(img).shape[:2]
  window_width, window_height = window_size
  patch_width, patch_height = patch_size

  fds = []
  anchors = []

  for y in range(0, img_height - window_height + 1, step_size):
      for x in range(0, img_width - window_width + 1, step_size):
          resized_patch = get_resized_patch(img, (x, y, x+window_height, y+window_width), patch_size)
          hog_features = get_hog(resized_patch)
          fds.append(hog_features)
          anchors.append((x, y))
  # convert to numpy arrays
  fds = np.stack(fds)
  anchors = np.stack(anchors)
  return fds, anchors