#!python


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
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    items1 = items[:len(items) // 2]
    items2 = items[len(items) // 2:]
    # Sort each half using any other sorting algorithm
    items1.sort()
    items2.sort()
    # Merge sorted halves into one list in sorted order
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


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if list is so small it's already sorted (base case)
    if len(items) < 2:
        return
    # Split items list into approximately equal halves
    items1 = items[:len(items) // 2]
    items2 = items[len(items) // 2:]
    # Sort each half using any other sorting algorithm
    # Sort each half by recursively calling merge sort
    merge_sort(items1)
    merge_sort(item2)
    # Merge sorted halves into one list in sorted order
    # Option 1:
    # merge(items1, items2)
    # Option 2:
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


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


array1 = [0, 1, 5, 9, 10]
array2 = [2, 5, 6, 7, 8]
large_array = [9, 10, 4, 6, 8, 9, 40, 84, 1]

# print(merge(array1, array2))
print((split_sort_merge(large_array)))
