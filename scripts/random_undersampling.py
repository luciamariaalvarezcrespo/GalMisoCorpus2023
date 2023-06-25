# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 25/06/2023
# Description: Random Undersampling
# Python version: 3.10.6

import numpy as np

# Entrances: X and y, being X the dataset and y the labels.
# Outputs: X_resampled and y_resampled
def random_undersampling(X, y):

    # Count the number of samples of each class
    counts = np.bincount(y)
    minority_class = np.argmin(counts)
    minority_count = counts[minority_class]

    # Obtain the indices of the majority class
    majority_indices = np.where(y == 1 - minority_class)[0]

    # Randomly select indices of the majority class to keep
    random_indices = np.random.choice(majority_indices, size=minority_count, replace=False)

    # Combine the minority class indices with the randomly selected majority class indices
    indices = np.concatenate([np.where(y == minority_class)[0], random_indices])

    # Obtain the resampled dataset
    X_resampled = X[indices]
    y_resampled = y[indices]

    return X_resampled, y_resampled
