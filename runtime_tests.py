from tests.test_sorted import ManualSortCases, BigInputsSortCase,\
                              BigElementsSortCase, AlreadySortedSortCase,\
                              InverselySortedSortCase
import timeit
import matplotlib.pyplot as plt
import numpy as np


####################
# This class measures the runtime of a very diverse type of inputs.
####################

class TimeTests:
    """ Measures the time of running of a bunch of inputs """

    def __init__(self):
        self.max_exponent = 5
        self.num_repeats = 100  # the higher the more accuracy in measuring time
        self.num_test_points = 8

    def run(self):
        self.time_big_inputs()
        # self.time_big_elements()
        # self.time_already_sorted()
        # self.time_inversely_sorted()

    def time_big_inputs(self):
        n_elems_range = np.linspace(1, 2**self.max_exponent, num=self.num_test_points, dtype=int).tolist()
        times_merge = []
        times_counting = []
        sort_case= BigInputsSortCase('merge')
        for i,n_elems in enumerate(n_elems_range):
            print(i)
            sort_case.setup(n_elems=n_elems, max_elem=n_elems)
            print('max:' + str(max(sort_case.test_input)))
            elapsed_time = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            times_merge.append(elapsed_time)
        sort_case = BigInputsSortCase('counting')
        for i, n_elems in enumerate(n_elems_range):
            print(i)
            sort_case.setup(n_elems=n_elems, max_elem=n_elems)
            elapsed_time = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            times_counting.append(elapsed_time)

        # plot both
        plt.plot(n_elems_range, times_merge, color='red', label='Merge sort', linestyle='-', marker='o')
        plt.plot(n_elems_range, times_counting, color='blue', label='Counting sort', linestyle='-', marker='o')
        plt.title('Big Inputs case')
        plt.xlabel('size (length) of the input')
        plt.ylabel('ms.')
        plt.legend(loc='upper left', frameon=True)
        plt.show()

    def time_big_elements(self):
        max_value_range = np.linspace(1, 2**self.max_exponent, num=self.num_test_points, dtype=int).tolist()
        times_merge = []
        times_counting = []
        sort_case= BigElementsSortCase('merge')
        for max_value in max_value_range:
            sort_case.setup(max_value=max_value)
            elapsed_time = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            times_merge.append(elapsed_time)
        sort_case = BigElementsSortCase('counting')
        for max_value in max_value_range:
            sort_case.setup(max_value=max_value)
            elapsed_time = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            times_counting.append(elapsed_time)

        # plot both
        plt.plot(max_value_range, times_merge, color='red', label='Merge sort', linestyle='-', marker='o')
        plt.plot(max_value_range, times_counting, color='blue', label='Counting sort', linestyle='-', marker='o')
        plt.title('Big Elements case')
        plt.xlabel('maximum size of th elements, k')
        plt.ylabel('ms.')
        plt.legend(loc='upper left', frameon=True)
        plt.show()

    def time_already_sorted(self):
        max_value_range = np.linspace(1, 2**self.max_exponent, num=self.num_test_points, dtype=int).tolist()
        times_diff_merge = []
        times_diff_counting = []
        for n_elems in max_value_range:
            sort_case = AlreadySortedSortCase('merge')
            sort_case.setup(n_elems=n_elems)
            elapsed_time_sorted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            sort_case = ManualSortCases('merge')
            sort_case.setup(np.random.permutation(n_elems).tolist())
            elapsed_time_permuted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            diff_merge = elapsed_time_permuted - elapsed_time_sorted
            print(diff_merge)
            times_diff_merge.append(diff_merge)
        for n_elems in max_value_range:
            sort_case = AlreadySortedSortCase('counting')
            sort_case.setup(n_elems=n_elems)
            elapsed_time_sorted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            sort_case = ManualSortCases('counting')
            sort_case.setup(np.random.permutation(n_elems).tolist())
            elapsed_time_permuted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            diff_count = elapsed_time_permuted - elapsed_time_sorted
            print(diff_count)
            times_diff_counting.append(diff_count)

        # plot both
        plt.plot(max_value_range, times_diff_merge, color='red', label='Merge sort', linestyle='-', marker='o')
        plt.plot(max_value_range, times_diff_counting, color='blue', label='Counting sort', linestyle='-', marker='o')
        plt.title('Already Sorted case')
        plt.xlabel('size (length) of the input')
        plt.ylabel(r'$RT_{PERMUTED} - RT_{SORTED}$ [ms.]')
        plt.legend(loc='upper left', frameon=True)
        plt.show()

    def time_inversely_sorted(self):
        max_value_range = np.linspace(1, 2**self.max_exponent, num=self.num_test_points, dtype=int).tolist()
        times_diff_merge = []
        times_diff_counting = []
        for n_elems in max_value_range:
            sort_case = InverselySortedSortCase('merge')
            sort_case.setup(n_elems=n_elems)
            elapsed_time_sorted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            sort_case = ManualSortCases('merge')
            sort_case.setup(np.random.permutation(n_elems).tolist())
            elapsed_time_permuted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            diff_merge = elapsed_time_permuted - elapsed_time_sorted
            print(diff_merge)
            times_diff_merge.append(diff_merge)
        for n_elems in max_value_range:
            sort_case = InverselySortedSortCase('counting')
            sort_case.setup(n_elems=n_elems)
            elapsed_time_sorted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            sort_case = ManualSortCases('counting')
            sort_case.setup(np.random.permutation(n_elems).tolist())
            elapsed_time_permuted = min(timeit.repeat(sort_case.sort, number=1, repeat=self.num_repeats))*1000
            diff_count = elapsed_time_permuted - elapsed_time_sorted
            print(diff_count)
            times_diff_counting.append(diff_count)

        # plot both
        plt.plot(max_value_range, times_diff_merge, color='red', label='Merge sort', linestyle='-', marker='o')
        plt.plot(max_value_range, times_diff_counting, color='blue', label='Counting sort', linestyle='-', marker='o')
        plt.title('Inversely Sorted case')
        plt.xlabel('size (length) of the input')
        plt.ylabel(r'$RT_{PERMUTED} - RT_{SORTED}$ [ms.]')
        plt.legend(loc='upper left', frameon=True)
        plt.show()

if __name__ == "__main__":
    TimeTests().run()