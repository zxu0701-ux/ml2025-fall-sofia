import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter N: ").strip())
    if N <= 0:
        return

    k = int(input("Enter k: ").strip())
    if k <= 0:
        return

    xs = []
    ys = []
    for i in range(N):
        x_val = float(input(f"Point {i+1} - enter x: ").strip())
        y_val = float(input(f"Point {i+1} - enter y: ").strip())
        xs.append(x_val)
        ys.append(y_val)

    X_train = np.array(xs, dtype=float).reshape(-1, 1)
    y_train = np.array(ys, dtype=float)

    if k > N:
        return

    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X_train, y_train)

    X_query = float(input("Enter X value to predict Y using k-NN regression: ").strip())
    X_query_arr = np.array([[X_query]])

    y_pred = knn.predict(X_query_arr)[0]

    label_variance = np.var(y_train)

    print(f"Predicted Y for X = {X_query}: {y_pred}")
    print(f"Variance of labels (y) in the training dataset: {label_variance}")


if __name__ == "__main__":
    main()