import numpy as np

def sort(A):
    """
    Sort a list or array using Counting Sort.
    The code style is not following the Python conventions
     to make it more compatible to the syntax of the pseudocode shown in class.

    :param A:      Must contain comparable elements to be sorted.
    :return:       A sorted array containing the elements of the input array.
    """

    k = max(A)
    L = len(A)

    # initialize C to zeros
    C = np.empty(shape=(k+1,))
    for i in range(k+1):
        C[i] = 0

    # make C[i] contain the number of elements equal to i
    for i in range(L):
        C[A[i]] += 1

    # make C[i] contain the number of elements lower or equal to i
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    # place every element of A in its sorted position
    B = np.empty_like(A)
    for i in range(L):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B