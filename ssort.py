# THE SELECTION SORT ALGORITHM
# Input: list of item
# Output: sorted list of item


from load import load_numubers


def selection_sort(list):
    """
    Takes a list of items and returns of a sorted list
    Takes an overall run time of O(n^2)
    """
    if len(list) <= 1:
        return list
    else:
        unsorted_list = list.copy()  # Make a copy of the input list(REDUNDANT)
        sorted_list = []
        while len(unsorted_list) > 0:  # Takes a runtime of O(n)
            min = find_min(unsorted_list)
            sorted_list.append(min)
            unsorted_list.remove(min)
        return sorted_list


def find_min(list):
    """
    Takes a list of item and 
    Returns the minimum item in the list
    """
    min = list[0]
    for i in range(1, len(list)):  # Takes a runtime of O(n)
        if list[i] < min:
            min = list[i]
    return min


# list = [5, 1, 4, 9, 3, 14, 7, 2, 23, 17, 3]
list = load_numubers("10000.txt")
print("Started sorting...")
sorted_list = selection_sort(list)
print("Ended...")
