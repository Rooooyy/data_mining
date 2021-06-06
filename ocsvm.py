import numpy as np
import matplotlib.pyplot as plt
import sklearn.svm as svm

X = np.load('feature_vector_v1.npy')

model = svm.OneClassSVM(nu=0.1, kernel='rbf', gamma=0.1)
model.fit(X)

Y = model.predict(X)

