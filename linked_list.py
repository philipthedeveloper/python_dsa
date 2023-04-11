class Node:
    """
      An object for storing a single node of a linked list.
      Model two attr - data and the link to the next node in the list
    """
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"


class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

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
        """
          Search for the first node containing the data that matches the key
          Return the node or None if not found
        """
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

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def remove_at_index(self, index):
        if index < 0:
            return None
        if index > self.size() - 1:
            return None
        if index == 0:
            return self.remove(self.head.data)
        else:
            current = self.head
            previous = None
            position = index

            while position >= 1:
                previous = current
                current = current.next_node
                position -= 1

            previous.next_node = current.next_node
            return current

    def node_at_index(self, index):

        if index > self.size() - 1:
            return None
        else:
            current = self.head
            position = index

            while position >= 1:
                current = current.next_node
                position -= 1

            return current

    def __str__(self) -> str:
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node
        return " -> ".join(nodes)


l = LinkedList()
# l.add(1)
# l.add(20)
# l.add(2)
# l.add(45)
# l.add(3)

# print(l)
# print(l.size())
# print(l.search(20))
# l.insert(4, 3)
# print(l)
# print(l.remove_at_index(9))
# print(l)
# print(l.node_at_index(5))
# print(l.remove_at_index(5))
# print(l)
# l.remove(45)
# print(l)
# l.remove(1)
# print(l)
