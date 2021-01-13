# Cu Set of vulnerable connected components
# max_T total number of nodes being targeted
# T_size Size of the target region
# alpha Creation cost of one edge

def greedySelect(Cu, max_T, T_size, alpha):
    result = []
    for CC in Cu:
        if len(CC) == T_size:
            if len(CC)*(1 - (max_T / T_size)) > alpha:
                result.append(CC)
        else:
            if len(CC) > alpha:
                result.append(CC)
    return result