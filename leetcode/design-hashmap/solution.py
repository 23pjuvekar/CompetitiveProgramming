class MyHashMap:

    def __init__(self):
        self.array = [[] for _ in range(100)]
        

    def put(self, key: int, value: int) -> None:
        for item in self.array[key % 100]:
            if item[1] == key:
                item[0] = value
                return
        self.array[key % 100].append([value, key])
        
    def get(self, key: int) -> int:
        for item in self.array[key % 100]:
            if item[1] == key:
                return item[0]
        return -1
        
    def remove(self, key: int) -> None:
        for item in self.array[key % 100]:
            if item[1] == key:
                self.array[key % 100].remove(item)
        
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
