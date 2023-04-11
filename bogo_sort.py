import random


def sorted(list):
    # #  Using recursion
    # if len(list) <= 1:
    #     return True
    # return list[0] < list[1] and sorted(list[1:])

    # Using loop
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def bogo_sort(list):
    attempt = 0
    while not sorted(list):
        print(attempt)
        random.shuffle(list)
        attempt += 1
    return list


# list = [5, 1, 4, 9, 3, 14, 7, 2, 23, 17]
list = [5, 1, 4, 9, 3]
print(bogo_sort(list))
