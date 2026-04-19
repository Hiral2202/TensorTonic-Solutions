import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)
    total = len(y_left) + len(y_right)

    if total == 0:
        return 0.0
    
    values_l, counts_l = np.unique(y_left, return_counts=True)
    gini_left = 1 - np.sum(np.square(counts_l/np.sum(counts_l)))
    
    values_r, counts_r = np.unique(y_right, return_counts=True)
    gini_right = 1 - np.sum(np.square(counts_r/np.sum(counts_r)))

    gini_split = (len(y_left)/total * gini_left) + (len(y_right)/total * gini_right)

    return gini_split
    pass