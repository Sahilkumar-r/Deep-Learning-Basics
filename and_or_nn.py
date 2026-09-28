import numpy as np


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


class SingleLayerNN:
    def __init__(self, n_inputs, learning_rate=0.5, seed=0):
        rng = np.random.default_rng(seed)
        self.W = rng.normal(scale=0.5, size=(n_inputs, 1))
        self.b = np.zeros((1, 1))
        self.lr = learning_rate

    def forward(self, X):
        return sigmoid(X @ self.W + self.b)

    def loss(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def backward(self, X, y_true, y_pred):
        n = X.shape[0]
        dloss_dpred = 2 * (y_pred - y_true) / n
        dpred_dz = y_pred * (1 - y_pred)
        dz = dloss_dpred * dpred_dz
        dW = X.T @ dz
        db = dz.sum(axis=0, keepdims=True)
        return dW, db

    def train(self, X, y, epochs=5000, log_every=1000):
        for epoch in range(1, epochs + 1):
            y_pred = self.forward(X)
            dW, db = self.backward(X, y, y_pred)
            self.W -= self.lr * dW
            self.b -= self.lr * db
            if epoch % log_every == 0 or epoch == 1:
                print(f"  epoch {epoch:5d}  loss = {self.loss(y, y_pred):.6f}")

    def predict(self, X):
        return (self.forward(X) >= 0.5).astype(int)


def run_gate(name, X, y):
    print(f"Training {name} gate")
    model = SingleLayerNN(n_inputs=2, learning_rate=0.5, seed=1)
    model.train(X, y)

    probs = model.forward(X)
    preds = model.predict(X)

    print(f"\n{name} results")
    print("  x1 x2 | target | prob   | pred")
    for xi, ti, pi, di in zip(X, y, probs, preds):
        print(f"   {int(xi[0])}  {int(xi[1])} |   {int(ti[0])}    | {pi[0]:.4f} |  {di[0]}")
    print(f"  weights = {model.W.ravel().round(4)}, bias = {model.b.ravel().round(4)}")
    print(f"  accuracy = {(preds == y).mean() * 100:.1f}%\n")


def main():
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y_and = np.array([[0], [0], [0], [1]], dtype=float)
    y_or = np.array([[0], [1], [1], [1]], dtype=float)

    run_gate("AND", X, y_and)
    run_gate("OR", X, y_or)


if __name__ == "__main__":
    main()
