import numpy as np
from quart import jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class CustomMLP:
    def __init__(self, layer_sizes, activation='relu'):
        self.layer_sizes = layer_sizes
        self.activation = activation
        self.weights = [np.random.randn(y, x) * np.sqrt(2/x) for x, y in zip(layer_sizes[:-1], layer_sizes[1:])]
    def activate(self, x):
        if self.activation == 'relu':
            return np.maximum(0, x)
        elif self.activation == 'sigmoid':
            return 1.0/(1.0 + np.exp(-x))

    def forward(self, X):
        self.a = [X]
        self.z = []
        for w in self.weights:
            self.z.append(np.dot(self.a[-1], w.T))
            self.a.append(self.activate(self.z[-1]))
        return self.a[-1]

    def backprop(self, X, y, learning_rate=0.0001):
        m = X.shape[0]
        dz = self.a[-1] - y
        dw = 1/m * np.dot(dz.T, self.a[-2])
        self.weights[-1] -= learning_rate * dw
        for i in range(len(self.weights)-2, -1, -1):
            dz = np.dot(dz, self.weights[i+1]) * ((self.a[i+1] > 0) if self.activation == 'relu' else (self.a[i+1] * (1 - self.a[i+1])))
            dw = 1/m * np.dot(dz.T, self.a[i])
            self.weights[i] -= learning_rate * dw

    def fit(self, X, y, epochs=500):
        for _ in range(epochs):
            self.forward(X)
            self.backprop(X, y)

    def partial_fit(self, X, y, epochs=100):
        self.fit(X, y, epochs)

    def predict(self, X):
        print("training")
        return np.argmax(self.forward(X), axis=1)

