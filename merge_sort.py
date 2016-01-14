import numpy as np

def sort(array):
    """
    Sort a list or array using Merge Sort.
    The code style is not following the Python conventions
     to make it more compatible to the syntax of the pseudocode shown in class.

    :param array:  Must contain comparable elements to be sorted.
    :return:       A sorted array containing the elements of the input array.
    """

    N = len(array)

    # a list of 1 element is considered sorted
    if N == 1:
        return array

    # DIVIDE the list into two sublists
    wall = N // 2  # integer division
    array1 = array[0:wall]
    array2 = array[wall:N]

    # apply merge sort recursively to each list
    array1 = sort(array1)
    array2 = sort(array2)

    # MERGE the two lists, which are now sorted.
    i = 0
    j = 0
    len_array1 = len(array1)
    len_array2 = len(array2)
    s = 0
    sorted_array = np.empty(shape=(len_array1+len_array2))  # loop through both arrays
    while i < len_array1 and j < len_array2:                # and put the smallest
        array1_elem = array1[i]                             # element first
        array2_elem = array2[j]
        if array1_elem <= array2_elem:
            sorted_array[s] = array1_elem
            s += 1
            i += 1
        else:
            sorted_array[s] = array2_elem
            s += 1
            j += 1
    # when one of the two arrays are finished looping, append the remaining one
    while j < len_array2:
        sorted_array[s] = array2[j]
        s += 1
        j += 1
    while i < len_array1:
        sorted_array[s] = array1[i]
        s += 1
        i += 1

    return sorted_array