###########################
#### Exercise Function ####
###########################
def barlow_loss(z1, z2, bn, lambd):
    '''
    return the barlow twins loss function for a pair of features. Makes use of the off_diagonal function.
    
    :param z1: first input feature
    :param z2: second input feature
    :param bn: nn.BatchNorm1d layer applied to z1 and z2
    :param lambd: trade-off hyper-parameter lambda
    '''
    
    z1_norm = bn(z1)
    z2_norm = bn(z2)
    c = torch.mm(z1_norm.t(), z2_norm) / z1_norm.shape[0]
    diagonal = torch.diag(c)
    ones = torch.ones_like(diagonal)
    diagonal_loss = torch.sum((diagonal - ones) ** 2)
    
    off_diagonal_c = off_diagonal(c)
    off_diagonal_loss = torch.sum(off_diagonal_c ** 2) * lambd
    
    return diagonal_loss + off_diagonal_loss
    
