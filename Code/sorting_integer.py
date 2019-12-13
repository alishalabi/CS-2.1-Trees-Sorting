#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n*k) where n is the length of input and k is unique values in input
    TODO: Memory usage: O(n)"""
    output = []
    # Find range of given numbers (minimum and maximum integer values)
    minimum_number = min(numbers)
    maximum_number = max(numbers)
    range_numbers = (maximum_number - minimum_number) + 1
    # Create list of counts with a slot for each number in input range
    all_counts = [0] * range_numbers
    # Loop over given numbers and increment each number's count
    for number in numbers:
        all_counts[number-minimum_number] += 1
    # Loop over counts and append that many numbers into output list
    for number in all_counts:
        while number > 0:
            output.append(number)
            number -= 1
    return output
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
