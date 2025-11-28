import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_positive_int(prompt: str) -> int:
    while True:
        val = input(prompt).strip()
        try:
            n = int(val)
            if n <= 0:
                raise ValueError
            return n
        except ValueError:
            print("Enter a positive integer.")

def read_pairs(count: int, set_name: str):
    X = np.empty((count, 1), dtype=float)
    y = np.empty((count,), dtype=int)
    for i in range(count):
        while True:
            try:
                x_val = float(input(f"{set_name} pair {i+1} - enter x: ").strip())
                break
            except ValueError:
                print("x must be a real number!")
        while True:
            try:
                y_val = int(input(f"{set_name} pair {i+1} - enter y (non-negative integer): ").strip())
                if y_val < 0:
                    raise ValueError
                break
            except ValueError:
                print("y must be a non-negative integer!")
        X[i, 0] = x_val
        y[i] = y_val
    return X, y

def main():
    N = read_positive_int("Enter N, number of training pairs: ")
    X_train, y_train = read_pairs(N, "Train")

    M = read_positive_int("Enter M, number of test pairs: ")
    X_test, y_test = read_pairs(M, "Test")

    k_max = min(10, N)
    best_k = 1
    best_acc = -1.0

    for k in range(1, k_max + 1):
        clf = KNeighborsClassifier(n_neighbors=k)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        if acc > best_acc:
            best_acc = acc
            best_k = k

    print(f"Best k: {best_k}")
    print(f"Test accuracy: {best_acc:.4f}")

if __name__ == "__main__":
    main()
