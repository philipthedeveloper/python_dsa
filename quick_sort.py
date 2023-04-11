from load import load_numubers
# def recursive_sum(numbers):
#     if not numbers:
#         return 0
#     print("Calling {}".format(numbers[1:]))
#     recursive_total = recursive_sum(numbers[1:])
#     print("Call to sum {} Returning %s + %s".format(numbers) %
#           (numbers[0], recursive_total))
#     return numbers[0] + recursive_total


# print(recursive_sum([1, 3, 5, 7, 9]))

def quick_sort(list):
    if len(list) <= 1:
        return list

    less_than_pivot = []
    greater_than_pivot = []

    pivot = list[0]

    for i in range(1, len(list)):
        if list[i] <= pivot:
            less_than_pivot.append(list[i])
        else:
            greater_than_pivot.append(list[i])

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


list = load_numubers("1000000.txt")
# list = [5, 1, 4, 9, 3, 14, 7, 2, 23, 17, 3]
print("Done loading...")
sorted_list = quick_sort(list)
print("Done sorting...")
# print(sorted_list)

# import random

# with open("10000.txt", "w") as file:
#     list = []
#     for i in range(1, 10001):
#         list.append(i)
#     random.shuffle(list)
#     for i in list:
#         file.write(f"{str(i)}\n")
