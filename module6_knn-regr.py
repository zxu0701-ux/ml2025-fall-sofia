import sys
import numpy as np

class KNNRegressor:
    def __init__(self, k: int):
        self.k = int(k)
        self.X = None
        self.y = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).reshape(-1)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must have the same number of rows.")
        self.X, self.y = X, y

    def predict_one(self, xq: float) -> float:
        if self.X is None:
            raise RuntimeError("Model is not fitted.")

        xq_vec = np.array([[float(xq)]], dtype=float)

        dists = np.linalg.norm(self.X - xq_vec, axis=1)

        nn_idx = np.argpartition(dists, kth=self.k - 1)[: self.k]
        return float(np.mean(self.y[nn_idx]))


def read_positive_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt).strip())
            if val <= 0:
                raise ValueError
            return val
        except ValueError:
            print("Enter a positive integer.", file=sys.stderr)

def read_float(prompt: str) -> float:
    while True:
        try:

            tokens = input(prompt).strip().replace(",", " ").split()
            if len(tokens) != 1:
                raise ValueError
            return float(tokens[0])
        except ValueError:
            print("Enter a valid real number.", file=sys.stderr)

def main():
    N = read_positive_int("Enter N : ")
    k = read_positive_int("Enter k : ")

    if k > N:
        print("Error: k must be ≤ N.")
        return


    Xs = np.empty(N, dtype=float)
    Ys = np.empty(N, dtype=float)

    print(f"Please provide {N} points. ")

    for i in range(N):
        xi = read_float(f"Point {i+1} — x: ")
        yi = read_float(f"Point {i+1} — y: ")
        Xs[i] = xi
        Ys[i] = yi

    X_query = read_float("Enter X: ")

    model = KNNRegressor(k=k)
    model.fit(Xs, Ys)
    y_pred = model.predict_one(X_query)

    print(f"Predicted Y (k-NN, k={k}) at X={X_query}: {y_pred}")

if __name__ == "__main__":
    main()