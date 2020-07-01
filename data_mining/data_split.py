"""
@author Mehmet Emin Yıldırım

Functions:
    train_test_split: splitting train and test data from original dataset
"""
import random


def train_test_split(X, y, test_rate=0.3, random_state=None):
    if random_state:
        random.seed(random_state)
    size = len(X)
    test_size = int(size * test_rate)
    X_train = X.copy()
    y_train = y.copy()
    X_test = []
    y_test = []

    while(test_size != 0):
        index = random.randint(0, size-1)
        X_test.append(X_train[index])
        y_test.append(y_train[index])
        del X_train[index]
        del y_train[index]
        size -= 1
        test_size -= 1

    return X_train, X_test, y_train, y_test
