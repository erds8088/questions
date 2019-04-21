"""
    实现一个LRU(least recently used)算法
"""

class LRUCache(object):
    def __init__(self, size):
        self.size = size
        self.cache = dict()
        self.keys = list()  # 列表尾部代表最近使用的key，每次达到长度上限时，删除keys[0]

    def get(self, key):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        return None

    def set(self, key, value):
        if key in self.keys:
            self.keys.remove(key)
        elif len(self.keys) == self.size:
            expried_key = self.keys[0]
            self.cache.pop(expried_key)
            self.keys = self.keys[1:]
        self.cache[key] = value
        self.keys.append(key)


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.set("a", 1)
    lru.set("a", 2)
    lru.set("b", 1)
    lru.set("c", 3)
    lru.set("d", 4)
    print(lru.get("c"))
    print(lru.cache, lru.keys)
