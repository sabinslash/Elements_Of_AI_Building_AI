import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3  # classify our test items based on the classes of 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # get indices of k nearest neighbors
        nearest_indices = np.argsort(distances)[:k]

        # get the classes of the k nearest neighbors
        nearest_classes = y_train[nearest_indices]

        # calculate the majority class among the nearest neighbors
        majority_class = int(np.round(np.mean(nearest_classes)))

        y_predict[i] = majority_class

        # create a line connecting the points for the chart
        # you may change this to do the same for all the k nearest neighbors if you like
        # but it will not be checked in the tests
        lines.append(np.stack((test_item, X_train[nearest_indices[0]])))

    print(y_predict)

main(X_train, X_test, y_train, y_test)