# THE MERGE SORT ALGORITHM
# Input: list of item
# Stopping condition: A list of size 0 or 1
# OPERATIONS
# Split
# Sort
# return sorted list

from load import load_numubers


def mergesort(list):
    """
    Takes a list of items and returns of a sorted list
    Takes an overall run time of O(nlogn)
    """

    # Sorting operation is performed on only a list of size > 1
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = mergesort(left_half)
    right = mergesort(right_half)
    return merge(left, right)


def split(list):
    """
    Takes a list of item and 
    returns two lists of item half the size of the original list
    Take an overall runtime of O(logn)
    """
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right


def merge(left, right):
    """
    Takes two lists and 
    returns a single(sorted) list from the original lists
    Takes an overall runtime of O(n)
    """
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


# newList = [7, 5, 4, 8, 9, 2, 1, 11]
newList = load_numubers("10000.txt")
print("Started sorting...")
sortedList = mergesort(newList)
# print(sortedList)
