from load import load_numubers


def merge_sort(list):
    """
      Sort a list in ascending order.
      Returns a new sorted list

      Divide: Find the midpoint of the list and divide into sublist
      Conquer: Recursively sort the sublists created in previous step
      Combine: Merge the sorted sublists created in previous step
    """
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) runtime
    """
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


# def verify_sorted(list):
#     n = len(list)

#     if n == 0 or n == 1:
#         return True

#     return list[0] <= list[1] and verify_sorted(list[1:])

# def merge_sort(list):
#     if len(list) <= 1:
#         return list

#     midpoint = len(list) // 2
#     left_half = list[:midpoint]
#     right_half = list[midpoint:]
#     left_list = merge_sort(left_half)
#     right_list = merge_sort(right_half)

#     left_index = 0
#     right_index = 0

#     sorted = []
#     while left_index < len(left_list) and right_index < len(right_list):
#         if left_list[left_index] < right_list[right_index]:
#             sorted.append(left_list[left_index])
#             left_index += 1
#         else:
#             sorted.append(right_list[right_index])
#             right_index += 1
#     sorted += left_list[left_index:]
#     sorted += right_list[right_index:]
#     return sorted


# list = [34, 53, 2, 64, 26, 12, 67, 8, 90, 78, 89, 34, 26]
# alist = [2, 7, 5, 3]
list = load_numubers("1000000.txt")
print("Done loading...")
l = merge_sort(list)
print("Done sorting...")
# is_sorted = verify_sorted(l)
# print(is_sorted)
print(l)
