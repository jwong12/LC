class DLinkedNode(object):
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _append_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _remove_last_node(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._append_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove_node(node)
            self._append_to_head(node)
            node.value = value
        else:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value
            self.cache[key] = new_node
            self._append_to_head(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._remove_last_node()
                del self.cache[tail.key]
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1))  # cache is {1 = 1}
    print(lRUCache.put(2, 2))  # cache is {1 = 1, 2 = 2}
    print(lRUCache.get(1))  # return 1
    print(lRUCache.put(3, 3))  # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
    print(lRUCache.get(2))  # returns - 1(not found))
    print(lRUCache.put(4, 4))  # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
    print(lRUCache.get(1))  # return -1(not found))
    print(lRUCache.get(3))  # return 3
    print(lRUCache.get(4))  # return 4
