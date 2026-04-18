import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y = np.asarray(y)
    values, counts = np.unique(y, return_counts = True)

    if(len(values)==1):
        return 0.0

    n = len(y)
    entropy = 0.0

    entropy = -np.sum((counts/n) @ np.log2(counts/n))

    return entropy
    pass