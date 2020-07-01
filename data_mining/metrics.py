"""
@author Mehmet Emin Yıldırım

Functions:
    accuracy_score: calculates accuracy score
    confusion_matrix: generates confusion matrix
"""
import numpy as np


def accuracy_score(y_test, y_pred):
    size = len(y_test)
    count = 0
    for i in range(size):
        if(y_test[i] == y_pred[i]):
            count += 1
    return count / size


def confusion_matrix(y_test, y_pred):
    labels = []
    for i in (y_test):
        if i not in labels:
            labels.append(i)
    for i in (y_pred):
        if i not in labels:
            labels.append(i)
    labels.sort()
    confusion_matrix = np.zeros((len(labels), len(labels)), dtype=int)
    for i in range(len(y_test)):
        true_index = labels.index(y_test[i])
        pred_index = labels.index(y_pred[i])
        confusion_matrix[true_index][pred_index] += 1
    return confusion_matrix
