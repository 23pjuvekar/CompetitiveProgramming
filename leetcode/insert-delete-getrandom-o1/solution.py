class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.data = []
        
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.data) # New position in data
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # map val:index
        # data 
        
        data_last_ele_val = self.data[-1] # last element of data
        map_remove_index = self.map[val] # index of element to remove

        self.map[data_last_ele_val] = map_remove_index # change map to point to removed index place
        self.data[map_remove_index] = data_last_ele_val # update data to have last element now

        self.data.pop()

        self.map.pop(val)
        return True


        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
