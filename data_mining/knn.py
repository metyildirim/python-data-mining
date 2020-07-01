"""
@author Mehmet Emin Yıldırım

Classes:
    KNNClassifier: classifies data using k-nearest-neighbors algorithm
"""
import math
import numpy as np


class KNNClassifier:
    def __init__(self, n_neighbors=5, metric='minkowski'):
        self.n_neighbors = n_neighbors
        if metric == 'minkowski':
            self.m = 3
        elif metric == 'euclidean':
            self.m = 2
        elif metric == 'manhattan':
            self.m = 1
        else:
            raise ValueError("metric '{}' not valid!".format(metric))

    def fit(self, X_train, y_train):
        self.X = np.asarray(X_train)
        self.y = y_train

    def predict(self, X_test):
        X_test = np.asarray(X_test)
        y_pred = []
        predict_count = 0
        total = len(X_test)
        for i in X_test:
            neighbor_indices = []
            distances = self.__calculate_distances(i)
            for i in range(self.n_neighbors):
                min_index = distances.argmin()
                neighbor_indices.append(min_index)
                distances = np.delete(distances, min_index)
            neighbor_labels = np.asarray([self.y[i] for i in neighbor_indices])
            labels, counts = np.unique(neighbor_labels, return_counts=True)
            predict_count += 1
            print("predicted {} in total {}".format(predict_count, total))
            y_pred.append(labels[counts.argmax()])
        return y_pred

    def __calculate_distances(self, i):
        return np.power(np.sum(np.power(np.absolute(np.subtract(i, self.X)),
                        self.m), axis=1, dtype=float), 1 / self.m)
