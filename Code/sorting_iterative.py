#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: Best case - O(1): first item out of order
    Running time: Worst case - O(n): all items in order
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check that all adjacent items are in order, return early if so
    # Iterate through each item in array, omit final item
    for index in range(len(items) - 1):
        # Check if item is greater than or equal to following item (ie not in order)
        if items[index] > items[index + 1]:
            # Early exit
            return False
    # All items in order
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Repeat until all items are in sorted order
    # Iterate through each index in array
    for current_index in range(len(items) - 1):
        # Sub-iterate through each index up until target index
        for index in range(current_index):
            # If item is out of order
            if items[index] > items[index + 1]:
                # Swap adjacent items that are out of order
                items[index], items[index + 1] = items[index + 1], items[index]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Set counter
    counter = 0
    while counter < len(items):
        # Set lowest item of iteration
        current_lowest_item = items[counter]
        # Set index of remaining items
        current_lowest_index = counter
        # Iterate through remaining items
        for remaining_item in len([counter:len(items)]):
            # See if item is lower than current lowest
            if remaining_item < current_lowest:
                # Set current lowest value
                current_lowest_item = remaining_item
                # Set current lowest index
                current_lowest_index = items.index(remaining_item)
        # Swap index at counter with current lowest
        items[counter], items[current_lowest_index] = items[current_lowest_index], items[counter]
        # Increment counter
        counter += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
