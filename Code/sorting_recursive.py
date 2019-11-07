#!python
import random


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) in all conditions (where n is total items in both lists)
    Memory usage: O(1)average - some sorted_output resizing"""
    sorted_output = []
    # While there are still items in both lists
    while len(items1) > 0 and len(items2) > 0:
        # If first item in items1 is less or equal to first item in items2
        if items1[0] <= items2[0]:
            # Add first item in items 1 to sorted output
            sorted_output.append(items1[0])
            # Remove first item from items 2
            items1.pop(0)
        # If not, add item from item2 to sorted array
        else:
            sorted_output.append(items2[0])
            # Remove first item from items2
            items2.pop(0)
    # One of the lists is now empty, append every item in remaining list
    while len(items1) > 0:
        sorted_output.append(items1[0])
        items1.pop(0)
    while len(items2) > 0:
        sorted_output.append(items2[0])
        items2.pop(0)

    return sorted_output


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(2n*(n/2)^2)
    Memory usage: O(1)"""
    # Split items list into approximately equal halves
    middle_index = len(items) // 2
    items1 = items[:middle_index]
    items2 = items[middle_index:]
    # Sort each half using any other sorting algorithm
    items1.sort()
    items2.sort()
    # Merge sorted halves into one list in sorted order
    sorted_items = merge(items1, items2)

    # for index in range(len(items)):
    #     items[index] = sorted_items[index]
    # Equivalent to:
    items[:] = sorted_items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n*log(n))
    Memory usage: O(n*log(n))"""
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return items
    # Split items list into approximately equal halves
    middle_index = len(items) // 2
    items1 = items[:middle_index]
    items2 = items[middle_index:]
    # Sort each half using any other sorting algorithm
    # Sort each half by recursively calling merge sort
    merge_sort(items1)
    merge_sort(items2)
    # Merge sorted halves into one list in sorted order
    items[:] = merge(items1, items2)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n)
    Memory usage: O(n)"""
    # Instantiate two empty arrays to store items smaller and larger than pivot
    smaller_than_pivot = []
    larger_than_pivot = []
    # Find pivot: random method
    pivot_index = random.randint(low, high)
    pivot_item = items[pivot_index]
    # Iterate through items (using index)
    for index in range(low, high + 1):
        # As long as item is not pivot
        if items[index] != pivot_item:
            # Append to smaller array if smaller than pivot
            if items[index] < pivot_item:
                smaller_than_pivot.append(items[index])
            # Append to larger array if larger than pivot
            else:
                larger_than_pivot.append(items[index])
    # Move pivot item into final position [p] and return index p
    # Note: section not well understood, modeling off of https://github.com/lvreynoso/CS-2.1-Trees-Sorting/blob/master/Code/sorting_recursive.py
    # Note: coming to OH to better understand (was absent week of work)
    pivot_index = low + len(smaller_than_pivot)
    if len(smaller_than_pivot) > 0:
        items[low:pivot_index] = smaller_than_pivot
    items[pivot_index] = pivot_item
    if len(larger_than_pivot) > 0:
        items[pivot_index + 1:high + 1] = larger_than_pivot
    return pivot_index


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(nlog(n))
    Worst case running time: O(n^2) if random partition is first or last item
    Memory usage: O(n)"""
    # Check if high and low range bounds have default values (not given)
    if low == None:
        low = 0
    if high == None:
        high = 0
    # Check if list or range is so small it's already sorted (base case)
    if low >= high:
        return items
    # Partition items in-place around a pivot and get index of pivot
    pivot_index = partition(items, low, high)
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot_index - 1)
    quick_sort(items, pivot_index + 1, high)
    return items


array1 = [0, 1, 5, 9, 10]
array2 = [2, 5, 6, 7, 8]
large_array = [9, 10, 4, 6, 8, 9, 40, 84, 1]

# print(merge(array1, array2))
print((split_sort_merge(large_array)))
