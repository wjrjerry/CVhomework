# model parameters
[h,w] = img.shape # get width & height of image
num_vars = w*h    # number of variables = width * height
num_states = 2    # binary segmentation -> two states

# initialize factors (list of dictionaries), each factor comprises:
#   vars: array of variables involved
#   vals: vector/matrix of factor values
factors = []

# add unary factors
for u in range(w):
  for v in range(h):
    
    # TODO
    factors.append({'vars': np.array([u+v*w]), 'vals': np.array([1-img[v,u],img[v,u]])})

# add pairwise factors
alpha = 0.4 # smoothness weight
E = alpha*np.array([[1,0],[0,1]]) # energy matrix for pairwise factor
for u in range(w):
  for v in range(h):
    
    # TODO
    if u<w-1:
      factors.append({'vars': np.array([u+v*w,(u+1)+v*w]), 'vals': E})
    if v<h-1:
      factors.append({'vars': np.array([u+v*w,u+(v+1)*w]), 'vals': E})
