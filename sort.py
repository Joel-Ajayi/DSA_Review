from typing import Optional


class Sort:
    arr: list[int]

    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def bubble(self):
        arr = self.arr.copy()
        n = len(self.arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    # O(n^2)
    def selection(self):
        arr = self.arr.copy()
        n = len(self.arr)
        for i in range(n):
            # assuming array <= i is sorted
            min_index = i  # current front of array

            # find min in unsorted part array
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # remove the val
            arr[min_index], arr[i] = arr[i], arr[min_index]

        return arr

    def insertion(self):
        arr = self.arr.copy()
        n = len(self.arr)
        for i in range(1, n):
            # assuming array <= i is sorted
            insertion_val = arr[i]
            j = i - 1

            # compare the insertion index with the sorted part of the array
            while j >= 0 and insertion_val < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            # 2. INSERT: Place the key into the created gap.
            arr[j + 1] = insertion_val

        return arr

    def bucket(self):
        pass

    def merge_sort(self, init: Optional[list[int]] = None):
        arr = self.arr.copy() if init is None else init

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        us_left = arr[:mid]
        us_right = arr[mid:]

        left = self.merge_sort(us_left)
        right = self.merge_sort(us_right)

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]):
        sorted_arr = []

        li = ri = 0
        l = len(left) - 1
        r = len(right) - 1

        while li <= l and ri <= r:
            if left[li] <= right[ri]:
                sorted_arr.append(left[li])
                li += 1
            else:
                sorted_arr.append(right[ri])
                ri += 1

        sorted_arr.extend(left[li:])
        sorted_arr.extend(right[ri:])

        return sorted_arr

    # using last value as pivot
    def quick(self, arr: list[int], start_index=0, end: Optional[int] = None):
        end_index = len(self.arr) - 1 if end is None else end

        if start_index < end_index:
            pivot_index = end_index  # note: pivot has to be between start and end index
            swap_index = -1

            for i in range(start_index, end_index + 1):
                if arr[i] > arr[pivot_index]:
                    if swap_index == -1:
                        swap_index = i
                elif swap_index != -1:
                    arr[swap_index], arr[i] = arr[i], arr[swap_index]
                    swap_index += 1

            # swap
            if swap_index == -1:
                self.quick(arr, start_index, end_index - 1)
            else:
                arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
                self.quick(arr, start_index, swap_index - 1)
                self.quick(arr, swap_index + 1, end)

        return arr

    # for min heap
    def heapify(self, arr: list[int], heap_size: int, parent_index: int):
        """
        Ensures the subtree rooted at parent_index is a max-heap.
        This is a "top-down" heapify, also known as max_heapify or sift-down.
        """
        largest_index = parent_index  # Assume the parent is the largest
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        # Check if the left child exists and is greater than the current largest
        if left_child_index < heap_size and arr[left_child_index] < arr[largest_index]:
            largest_index = left_child_index

        # Check if the right child exists and is greater than the current largest
        if (
            right_child_index < heap_size
            and arr[right_child_index] < arr[largest_index]
        ):
            largest_index = right_child_index

        # If the largest element is not the parent, swap them
        if largest_index != parent_index:
            arr[parent_index], arr[largest_index] = (
                arr[largest_index],
                arr[parent_index],
            )
            # Recursively heapify the affected subtree
            self.heapify(arr, heap_size, largest_index)

    def heap_sort(self):
        """
        Performs the heap sort algorithm.
        """
        arr_copy = self.arr.copy()
        n = len(arr_copy)

        # 1. Build a min-heap from the unsorted list.
        # We start from the last non-leaf node and go up to the root.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr_copy, n, i)

        # 2. Extract elements one by one from the heap.
        for i in range(n - 1, 0, -1):
            # Move the current root (max element) to the end
            arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]

            # Call heapify on the reduced heap. The heap size is now 'i'.
            self.heapify(arr_copy, i, 0)

        return arr_copy

    # for 1 to n
    def minimumSwaps(self):
        arr = self.arr.copy()
        i = 0
        n = len(arr)

        while i < n:
            # Rule: for a value K, it should belong to index K-1
            # Incase K is zero?,
            # i = K-1
            k = arr[i]
            correct_index = k - 1
            if i != correct_index:
                arr[i], arr[correct_index] = arr[correct_index], arr[i]
            else:
                i += 1

        return arr


s = Sort([1, 5, 2, 4, 6, 7])

# print(s.bubble())
# print(s.selection())
# print(s.insertion())
# print(s.merge_sort())
# print(s.quick(s.arr))
print(s.minimumSwaps())
#
