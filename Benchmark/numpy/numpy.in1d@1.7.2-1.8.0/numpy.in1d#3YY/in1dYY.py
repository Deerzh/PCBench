import numpy as np

def main():
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([3, 4, 7])
    result = np.in1d(ar1=array1, ar2=array2)
    print(result)
if __name__ == '__main__':
    main()
