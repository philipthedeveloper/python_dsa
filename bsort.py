# THE BUBBLE SORT ALGORITHM
# Input: list of item
# Output: sorted list of item


def bubble_sort(list):
    """
    Takes a list of items and returns of a sorted list
    Takes an overall run time of O(n^2)
    """
    if len(list) <= 1:
        return list
    i = len(list) - 1
    while i > 0:  # Takes a runtime of O(n)
        j = 0
        while j < i:  # Takes a runtime of O(n)
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            j += 1
        i -= 1

    return list


list = [7, 5, 4, 8, 9, 2, 1, 11]
print("Started sorting...")
sorted_list = bubble_sort(list)
print(sorted_list)
