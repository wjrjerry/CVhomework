# model parameters (number of variables/states)
[num_vars,num_states] = unary.shape

# compute messages
msg = np.zeros([num_vars-1, num_states]) # (num_vars-1) x num_states matrix
for i in range(num_vars-2, -1, -1):
    
    # TODO 
    # compute messages for the chain structured Markov random field
    if i == num_vars-2 :
        msg[i] = np.max(pairwise * unary[i+1], axis = 1)
    else : 
        msg[i] = np.max(pairwise * unary[i+1] * msg[i+1], axis = 1)
        
        

# model parameters (number of variables/states)
[num_vars,num_states] = unary.shape

# compute messages
msg = np.zeros([num_vars-1, num_states]) # (num_vars-1) x num_states matrix
for i in range(num_vars-2, -1, -1):
    
    # TODO 
    # compute messages for the chain structured Markov random field
    if i == num_vars-2 :
        msg[i] = np.max(pairwise * unary[i+1], axis = 1)
    else : 
        msg[i] = np.max(pairwise * unary[i+1] * msg[i+1], axis = 1)