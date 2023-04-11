# THE INSERTION SORT ALGORITHM
# Input: list of item
# Output: sorted list of item


from load import load_numubers


def insertion_sort(list):
    """
    Takes a list of items and returns of a sorted list
    Takes an overall run time of O(n^2)
    """
    if len(list) <= 1:
        return list
    for i in range(1, len(list)):  # Takes a runtime of O(n)
        temp = list[i]  # O(1)
        j = i - 1  # O(1)
        while j > -1 and temp < list[j]:   # Takes a runtime of O(n)
            list[j + 1] = list[j]  # O(1)
            j -= 1  # O(1)
        list[j + 1] = temp  # 0(1)
    return list

# time complexity n * n = O(n^2)
# space complexity n * n = O(n^2)


# list = [6, 2, 5, 3, 4, 1]
# list = [6]
# newList = load_numubers("10000.txt")
# print("Started sorting...")
# sorted_list = insertion_sort(newList)
