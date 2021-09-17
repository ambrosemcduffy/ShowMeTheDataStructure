class Node(object):
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None
    

class LRU_Cache(object):
    def __init__(self, capacity=3):
        self.cache = dict()
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.n_entries = 0
    
    def put(self, key, value):
        if self.size() >= self.capacity:
            print("Over Capacity")
            self.pop()
        if self.head is None:
            self.cache[key] = Node(key, value)
            self.head = self.cache[key]
            self.tail = self.head
            self.n_entries += 1
            return
        self.cache[key] = Node(key, value)
        self.tail.next = self.cache[key]
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.n_entries += 1
        return
    
    def get(self, key):
        if key in self.cache:
            self.head = self.head.next
            self.tail.previous = self.tail
            self.tail = self.cache[key]
            return self.cache[key].value
        else:
            return -1
    
    def pop(self, out=0):
        if out == 0:
            value = self.head.value
            key = self.head.key
            del self.cache[key]
            self.head = self.head.next
            self.n_entries -= 1
            return value
        elif out == 1:
            value = self.tail.value
            self.tail = self.tail.previous
            self.n_entries -= 1
            return value
        else:
            print("incorrect value either 0 or 1")
            return None
    
    def size(self):
        return self.n_entries
        


cache = LRU_Cache(5)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)


print(cache.get(1))
print(cache.get(2))
print(cache.get(9))



cache.put(5, 5)
cache.put(6, 6)
print(cache.get(3))
#print(cache.head.value)
#print(cache.size())
