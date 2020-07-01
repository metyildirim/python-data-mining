"""
@author Mehmet Emin Yıldırım

Functions:
    min_max_normalization: normalize data using min-max normalization
"""


def min_max_normalization(X):
    for feature_index in range(len(X[0])):
        # finding min and max
        min = X[0][feature_index]
        max = X[0][feature_index]
        for row_index in range(1, len(X)):
            cell = X[row_index][feature_index]
            if cell < min:
                min = cell
            if cell > max:
                max = cell
        # updating data
        for row in X:
            try:
                row[feature_index] = (row[feature_index] - min) / (max - min)
            except ZeroDivisionError:
                row[feature_index] = row[feature_index] - min
