import numpy as np

def main():
    data = np.array([[0, 2], [1, 1], [2, 0]])
    cov_matrix = np.cov(data, y=None)
    print(cov_matrix)
if __name__ == '__main__':
    main()
