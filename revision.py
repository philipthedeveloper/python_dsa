# Creating a node class
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data is key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > self.size():
            return
        else:
            new_node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            prev = current
            next = prev.next_node

            new_node.next_node = next
            prev.next_node = new_node

            # prev = None # Optional
            # while position < index:
            #     prev = current
            #     current = current.next_node
            #     position += 1
            # new_node.next_node = current
            # prev.next_node = new_node

    def remove(self, key):
        current = self.head
        prev = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                prev.next_node = current.next_node
            else:
                prev = current
                current = current.next_node
        return current

    def node_at_index(self, index):
        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current

    def __repr__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current == self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node

        return " -> ".join(nodes)


"""
def merge_sort(list):

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    midpoint = len(list) // 2

    left_half = list[:midpoint]
    right_half = list[midpoint:]

    return left_half, right_half


def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    sorted_list += left[left_index:]
    sorted_list += right[right_index:]
    return sorted_list


def verify_sorted(list):
    # for i in range(len(list) - 1):
    #     if list[i] > list[i+1]:
    #         return False
    #     i += 1
    # return True

    if len(list) <= 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])


list = [34, 53, 2, 64, 26, 12, 67, 8, 90, 78, 89, 34, 26]
sorted = merge_sort(list)
is_sorted = verify_sorted(sorted)
print(is_sorted)
print(sorted)
"""


def linkedlist_merge_sort(linkedlist):
    if linkedlist.size() <= 1:
        return linkedlist

    left_half, right_half = split(linkedlist)
    print(f"left_half: {left_half}", f"right_half: {right_half}")
    left = linkedlist_merge_sort(left_half)
    right = linkedlist_merge_sort(right_half)
    print("\nMerging {:<5} => {:<4} left: {} ; right: {}\n".format(
        "", "", left, right))

    return merge(left, right)


def split(linkedlist):
    midpoint = linkedlist.size() // 2
    midnode = linkedlist.node_at_index(midpoint - 1)

    left_half = linkedlist
    right_half = LinkedList()
    right_half.head = midnode.next_node
    midnode.next_node = None

    return left_half, right_half


def merge(left, right):

    sorted = LinkedList()

    sorted.add(7)

    current = sorted.head

    left_head = left.head
    right_head = right.head

    while left_head or right_head:
        if left_head == None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head == None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
    head = sorted.head.next_node
    sorted.head = head
    print("\nReturning {:<3} => {:<4}{}\n".format("", "", sorted))
    return sorted


l = LinkedList()
l.add(4)
l.add(25)
l.add(12)
l.add(27)
l.add(18)
l.add(45)
l.add(6)
print(l)


sorted = linkedlist_merge_sort(l)
print(sorted)
