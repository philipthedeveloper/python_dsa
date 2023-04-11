from load import load_numubers


def selection_sort(list):
    if len(list) <= 1:
        return list
    else:
        unsorted_list = list.copy()
        sorted = []
        # attempt = 1
        while len(unsorted_list) > 0:
            smallest = find_smallest_and_index(
                unsorted_list)
            sorted.append(smallest)
            unsorted_list.remove(smallest)
        return sorted


def find_smallest_and_index(list):
    # attempts = attempt
    smallest = list[0]
    for i in range(1, len(list)):
        # print("attempts: %s" % attempts)
        if list[i] < smallest:
            smallest = list[i]
        # attempts += 1
    return smallest


list = [5, 1, 4, 9, 3, 14, 7, 2, 23, 17, 3]
# list = [5, 1, 4, 9, 3]


# def sorted(list):
#     if len(list) <= 1:
#         return True
#     return list[0] < list[1] and sorted(list[1:])

# list = load_numubers("10000.txt")
sorted_list = selection_sort(list)
# is_sorted = sorted(sorted_list)
# print(is_sorted)
print(sorted_list)
