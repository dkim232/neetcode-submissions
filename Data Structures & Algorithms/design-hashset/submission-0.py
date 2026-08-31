class MyHashSet:

    def __init__(self):
        self.arr = defaultdict(list)
        
    def add(self, key: int) -> None:
        hashkey = key % 11
        if key not in self.arr[hashkey]:#doesnt exist:
            self.arr[hashkey].append(key)
        else: #key does exist
            return
            

    def remove(self, key: int) -> None:
        hashkey = key % 11
        if key not in self.arr[hashkey]:#doesnt exist:
            return
        else: #key does exist
            self.arr[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        hashkey = key % 11
        if key not in self.arr[hashkey]:#doesnt exist:
            return False
        else: #key does exist
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)