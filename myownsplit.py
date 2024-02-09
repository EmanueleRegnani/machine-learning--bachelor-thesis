import numpy as np
import pandas as pd


X = np.arange(10)
y = np.arange(0,20,2)
print(X, y)

data = pd.DataFrame({'X': X, 'y': y})
X = data.iloc[:, 0]
y = data.iloc[:, 1]


def myownsplit_function(X, y):
    X_train, y_train, X_test, y_test = [], [], [], []

    for i in range(len(X)):
        if i%5 == 0:
            X_test.append(X.iloc[i])
            y_test.append(y.iloc[i])
        else:
            X_train.append(X.iloc[i])
            y_train.append(y.iloc[i])

    return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)

print(myownsplit_function(X, y))
