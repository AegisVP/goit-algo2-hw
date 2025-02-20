from DoubleLinkedList import DoubleLinkedList

class LRUCache:
    version = 1

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.list = DoubleLinkedList()

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.list.move_to_front(node)
            return node.data[1]
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.data = (key, value)
            self.list.move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                last = self.list.remove_last()
                if last:
                    del self.cache[last.data[0]]
            new_node = self.list.push(key, value)
            self.cache[key] = new_node

    def remove(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.list.remove(node)
            del self.cache[key]

    def clear(self):
        self.cache = {}
        self.list = DoubleLinkedList()
