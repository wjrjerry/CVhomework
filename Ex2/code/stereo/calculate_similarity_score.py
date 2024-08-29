###########################
#### Exercise Function ####
###########################
def calculate_similarity_score(infer_similarity_metric, Xl, Xr):
    """
    Computes the similarity score for two stereo image patches.

    Args:
        infer_similarity_metric (torch.nn.Module):  pytorch module object
        Xl (torch.Tensor): tensor holding the left image patch
        Xr (torch.Tensor): tensor holding the right image patch

    Returns:
        score (torch.Tensor): the similarity score of both image patches which is the dot product of their features
    """
    #######################################
    # -------------------------------------
    # TODO: ENTER CODE HERE (EXERCISE 7)
    # -------------------------------------
    Xl_feature = infer_similarity_metric.forward(Xl)
    Xr_feature = infer_similarity_metric.forward(Xr)
    score = torch.sum(Xl_feature * Xr_feature, dim=-1).squeeze()


    return score