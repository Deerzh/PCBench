import numpy as np

def main():
    np.set_printoptions()
    arr = np.array([0.123456789, 1.23456789, 12.3456789, np.nan, np.inf, -np.inf])
    print('Array:')
    print(arr)
if __name__ == '__main__':
    main()
