import numpy as np

def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    max_index = np.argmax(a, axis=1)
    print(max_index)
if __name__ == '__main__':
    main()
