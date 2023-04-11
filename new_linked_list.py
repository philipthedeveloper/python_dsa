class Node:
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
        new = Node(data)
        new.next_node = self.head
        self.head = new
        # if current is None:
        #   self.head = new
        # else:
        #   while current:
        #     if current.next_node == None:
        #       current.next_node = new
        #       return
        #     current = current.next_node

    def insert(self, data, index):
        if index == 0:
            return self.add(data)
        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            new_node.next_node = current.next_node
            current.next_node = new_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or None if not found

        Takes O(n)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node

        return None

    def remove_at_index(self, index):
        if index < 0:
            return None
        if index == 0:
            return self.remove(self.head.data)
        if index >= self.size():
            return None

        previous = None
        current = self.head
        position = index

        while position > 0 and current:
            previous = current
            current = current.next_node
            position -= 1

        previous.next_node = current.next_node
        return current

    def node_at_index(self, index):
        if index < 0:
            return None
        if index >= self.size():
            return None
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next_node
                position += 1
            return current

    def contains(self, key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next_node

        return False

    def index_of(self, key):
        current = self.head
        count = 0
        found = False

        while current and not found:
            if current.data == key:
                found = True
                return count
            else:
                current = current.next_node
                count += 1
        return -1

    def modify_at_index(self, index, key):
        if index < 0:
            return None

        if index >= self.size():
            return None

        current = self.head
        new_node = Node(key)

        if index == 0:
            new_node.next_node = current.next_node
            self.head = new_node
        else:
            position = 0
            previous = None

            while position < index:
                previous = current
                current = current.next_node
                position += 1

            new_node.next_node = current.next_node
            previous.next_node = new_node

    def __repr__(self) -> str:
        current = self.head
        nodes = []

        while current:
            if current == self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node

        return " -> ".join(nodes)


l = LinkedList()
l.add(4)
l.add(1)
l.add(14)
l.add(34)
l.add(18)
l.insert(26, l.size())
print(l)
print(l.contains(18))
print(l.index_of(14))
print(l.index_of(13))
l.modify_at_index(2, 35)
print(l)
