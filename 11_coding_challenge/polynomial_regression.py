import sys
import numpy as np
from sklearn import linear_model

def polynomial_regression():
    # Read first line
    first_line = sys.stdin.readline().strip().split(' ')
    F, H = [int(i) for i in first_line]

    train =[]
    test = []

    for i in range(H):
        line = sys.stdin.readline()
        numbers = line.strip().split(' ')
        train.append([float(f) for f in numbers])

    # Read T
    T = input()

    for i in range(int(T)):
        line = sys.stdin.readline()
        numbers = line.strip().split(' ')
        test.append([float(f) for f in numbers])

    # Build Linear Model
    train = np.mat(train)
    model = linear_model.LinearRegression()
    model.fit(train[:, 0:F], train[:, F])

    # Prediction
    for results in model.predict(np.mat(test)):
        print(results[0])

    return 0

if __name__ == '__main__':
    polynomial_regression()