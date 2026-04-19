import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train = np.asarray(y_train)
    X_test = np.asarray(X_test)
    if len(y_train)==0:
        return None
    elif len(y_train)==1:
        return np.array([y_train[0]]*len(X_test))

    values, counts = np.unique(y_train, return_counts = True)
    max_index = np.argmax(counts)
    max = values[max_index]

    return np.array([max]*len(X_test))
    pass