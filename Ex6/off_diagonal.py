###########################
#### Exercise Function ####
###########################
def off_diagonal(x):
    '''
    returns a flattened view of the off-diagonal elements of a square matrix x
    '''
    n, m = x.shape
    assert n == m
    
    # 去掉cross_correlation matrix的对角线
    # 因为同一个元素的相关系数是1
    # 可以类比ai导论的lab3
    
    off_diagonal = x[~np.eye(n, dtype=bool)].reshape(n, -1)
    return off_diagonal