# 分开验证集和训练集


def get_train_val_split(points, occupancies):
  ''' Split data into train and validation set.
  
  Args:
  points (torch.Tensor or np.ndarray): 3D coordinates of the points
  occupancies (torch.Tensor or np.ndarray): occupancy values for the points
  '''
  # 将输入分为训练集和验证集
  
  # Insert your code here
  train_set_len = int(0.8 * points.shape[0])
  data_set = np.concatenate((points, occupancies.reshape(-1,1)), axis = 1) # 合并
  np.random.shuffle(data_set)
  train_data, val_data = np.split(data_set, [train_set_len, ])
  train_points = train_data[:,0:3]
  train_occs = train_data[:,3]
  val_points = val_data[:,0:3]
  val_occs = val_data[:,3]
  # this converts the points and labels from numpy.ndarray to a pytorch dataset
  train_set = torch.utils.data.TensorDataset(torch.from_numpy(train_points), torch.from_numpy(train_occs))
  val_set = torch.utils.data.TensorDataset(torch.from_numpy(val_points), torch.from_numpy(val_occs))
  return train_set, val_set

train_set, val_set = get_train_val_split(points, occupancies)