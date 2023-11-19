
import numpy as np
import timeit


def with_for_loop(array) -> int:
    """ function that multiplies each element (element wise) in the array with 3"""
    for i in array:
        i = i*3
    return array


def with_np_sum(array) -> int:
    """ function that uses vectorized multiplication with 3"""
    return array * 3


def main():
    """main function to demonstrate efficiency"""
    #initialize array
    array = np.random.randint(0, 100, 1000000)
    #print some metadata of array
    print(f'shape of array: {array.shape}')
    print(f'size of array: {array.size}')
    print(f'data type of array: {array.dtype}')
    
    # print time for for loop, running function 100 times
    print(timeit.timeit(lambda: with_for_loop(array), number=100))

    # print time for vectorized solution running function 100 times
    print(timeit.timeit(lambda: with_np_sum(array), number=100))


if __name__ == "__main__":
    main()