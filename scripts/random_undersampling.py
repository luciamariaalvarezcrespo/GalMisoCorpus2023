# Author: Lucía María Álvarez Crespo (GitHub: @luciamariaalvarezcrespo)
# Last modified: 01/04/2024
# Description: Random Undersampling
# Python version: 3.10.6
# License: Mozilla Public License Version 2.0

import numpy as np

def random_undersampling(X, y):
    """
    Apply random undersampling to a dataset.

    Args:
        X (array-like): Dataset.
        y (array-like): Labels corresponding to the dataset.

    Returns:
        X_resampled (array-like): Subsampled dataset.
        y_resampled (array-like): Labels corresponding to the subsampled dataset.
    """

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
