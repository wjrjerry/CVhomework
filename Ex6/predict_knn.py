###########################
#### Exercise Function ####
###########################
def predict_knn(sample, train_data, train_labels, k):
    '''
    returns the predicted label for a specific validation sample
    
    :param sample: single example from validation set
    :param train_data: full training set as a single array
    :param train_labels: full set of training labels and a single array
    :param k: number of nearest neighbors used for k-NN voting
    '''
    
    data = train_data.reshape(NUM_SAMPLES, -1)
    sample_new = sample.reshape(1, -1)
    L1_distances = np.sum(np.abs(data - sample_new), axis=1)
    
    k_nearest_indices = np.argpartition(L1_distances, k)[:k]
    k_nearest_labels = train_labels[k_nearest_indices]
    return np.argmax(np.bincount(k_nearest_labels))
    
    
    # return None