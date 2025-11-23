import numpy as np
from sklearn.metrics import precision_score, recall_score

def read_int(prompt):
    while True:
        try:
            v = int(input(prompt).strip())
            return v
        except ValueError:
            print("Please enter an integer.")

def read_binary(prompt):
    while True:
        try:
            v = int(input(prompt).strip())
            if v in (0, 1):
                return v
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Please enter 0 or 1.")

def main():
    N = read_int("Enter N (positive integer): ")
    while N <= 0:
        print("N must be positive.")
        N = read_int("Enter N (positive integer): ")

    x = np.empty(N, dtype=np.int64)
    y = np.empty(N, dtype=np.int64)

    print("\nPlease provide N (x, y) binary points (x: ground truth, y: predicted).")
    for i in range(N):
        xi = read_binary(f"Point {i+1} - enter x (0/1): ")
        yi = read_binary(f"Point {i+1} - enter y (0/1): ")

        x[i] = xi
        y[i] = yi

    precision = precision_score(x, y, zero_division=0)
    recall = recall_score(x, y, zero_division=0)

    print("\nResults:")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")

if __name__ == "__main__":
    main()
