import unittest
import random
import numpy.testing
import merge_sort
import counting_sort

default_sorting_alg = 'merge'

####################
# Classes whose methods sort inputs of a particular type:
#  very large inputs, already sorted inputs, inversely sorted...
####################

class BaseSortCase:
    """
    Base class for SortCases. It just provides a method that sorts.
    Classes that inherit from this class provide SortCases with a given type of input. Should not be used directly.
    """

    def __init__(self, sorting_algorithm=default_sorting_alg):
        self.test_input = None
        self.n_elems = None
        self.max_value = None
        if sorting_algorithm == 'merge':
            self.sort_alg = merge_sort.sort
        elif sorting_algorithm == 'counting':
            self.sort_alg = counting_sort.sort
        else:
            raise NotImplementedError("Only 'merge' and 'counting' algorithms are implemented")

    def sort(self):
        return self.test_input, self.sort_alg(self.test_input)

class ManualSortCases(BaseSortCase):
    """ Bunch of methods where manually typed inputs are sorted. """

    def setup(self, array):
        """
        Set up the array to be sorted.
        :param array: Array to be sorted.
        """
        self.test_input = array

class BigInputsSortCase(BaseSortCase):
    """
    Sort case where VERY LARGE inputs are sorted.
    The length of the input and maximum value of the input is configurable with the method 'setup'.
    The elements consist of random values up to the maximum input.
    """

    def setup(self, n_elems, max_elem):
        """
        Set up the number of elements of the input of this Sort Case.
        :param n_elems: Number of elements that the input elements will have.
        :param max_value: Maximum value that the input elements will have.
        """
        self.n_elems = n_elems
        self.max_elem = max_elem
        self.test_input = []
        for _ in range(n_elems):
            self.test_input.append(random.randint(1, max_elem))

class BigElementsSortCase(BaseSortCase):
    """
    Sort case where inputs with VERY BIG elements are sorted.
    The length of the input is hardcoded to 2, but the maximum value is configurable with the method 'setup'.
    The other elements consist of random integers.
    """

    def setup(self, max_value):
        """
        Set up the maximum value of the input of this Sort Case.
        :param max_value: Maximum value that the input elements will have.
        """
        self.max_value = max_value
        self.test_input = [random.randint(1, max_value), max_value]

class AlreadySortedSortCase(BaseSortCase):
    """
    Sort case where the inputs are already in sorted order starting from 0 ([0, 1, 2, ..., 5]).
    The length of the input is configurable with the method 'setup'.
    """

    def setup(self, n_elems):
        """
        Set up the number of elements of the input of this Sort Case.
        :param n_elems: Number of elements that the input elements will have.
        """
        self.n_elems = n_elems
        self.test_input = list(range(n_elems))

class InverselySortedSortCase(BaseSortCase):
    """
    Sort case where the inputs are sorted in reverse order ending in 0 ([5, 4, 3, ..., 0]).
    The length of the input is configurable with the method 'setup'.
    """

    def setup(self, n_elems):
        """
        Set up the number of elements of the input of this Sort Case.
        :param n_elems: Number of elements that the input elements will have.
        """
        self.n_elems = n_elems
        self.test_input = list(range(n_elems))
        self.test_input.reverse()

####################
# Test cases that check that the sorting works fine in all cases.
####################

class TestManualCase(unittest.TestCase):
    """ Test Case to check that the sort works correctly for manually typed inputs. """

    def test_1(self):
        arr, hopefully_sorted = ManualSortCases.sort_1()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))  # compare with Python default's sort method

    def test_2(self):
        arr, hopefully_sorted = ManualSortCases.sort_2()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_3(self):
        arr, hopefully_sorted = ManualSortCases.sort_3()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

class TestBigInputsCase(unittest.TestCase):
    """ Test Case to check that the sort works correctly for VERY LARGE random inputs. """

    def setUp(self):
        self.sort_case = BigInputsSortCase()

    def test_1(self):
        self.sort_case.setup(n_elems=2**5)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_2(self):
        self.sort_case.setup(n_elems=2*10)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_3(self):
        self.sort_case.setup(n_elems=2**15)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_4(self):
        self.sort_case.setup(n_elems=2**20)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

class TestBigElementsCase(unittest.TestCase):
    """ Test Case to check that the sort works correctly for inputs with VERY BIG elements. """

    def setUp(self):
        self.sort_case = BigElementsSortCase()

    def test_1(self):
        self.sort_case.setup(max_value=2**5)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_2(self):
        self.sort_case.setup(max_value=2**10)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_3(self):
        self.sort_case.setup(max_value=2**15)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_4(self):
        self.sort_case.setup(max_value=2**20)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

class TestAlreadySorted(unittest.TestCase):
    """ Test Case to check that the sort works correctly for already sorted inputs. """

    def setUp(self):
        self.sort_case = AlreadySortedSortCase()

    def test_1(self):
        self.sort_case.setup(n_elems=2**5)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_2(self):
        self.sort_case.setup(n_elems=2**10)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_3(self):
        self.sort_case.setup(n_elems=2**15)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

class TestInverselySorted(unittest.TestCase):
    """ Test Case to check that the sort works correctly for inputs sorted from . """

    def setUp(self):
        self.sort_case = InverselySortedSortCase()

    def test_1(self):
        self.sort_case.setup(n_elems=2**5)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_2(self):
        self.sort_case.setup(n_elems=2**10)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))

    def test_3(self):
        self.sort_case.setup(n_elems=2**15)
        arr, hopefully_sorted = self.sort_case.sort()
        numpy.testing.assert_array_equal(hopefully_sorted, sorted(arr))
