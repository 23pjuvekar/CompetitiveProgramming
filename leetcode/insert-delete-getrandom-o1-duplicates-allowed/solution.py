import random

class RandomizedCollection:

    def __init__(self):
        self.vals = []  # List to store values
        self.indices = {}  # Dictionary to store indices of values

    def insert(self, val: int) -> bool:
        """Inserts a value into the collection."""
        is_new = val not in self.indices
        self.vals.append(val)
        if val in self.indices:
            self.indices[val].add(len(self.vals) - 1)
        else:
            self.indices[val] = {len(self.vals) - 1}
        return is_new

    def remove(self, val: int) -> bool:
        """Removes a value from the collection."""
        if val not in self.indices or not self.indices[val]:
            return False
        
        # Get an index of the value to be removed
        index_to_remove = self.indices[val].pop()
        last_val = self.vals[-1]

        # If the value to remove is not the last one in the list
        if index_to_remove != len(self.vals) - 1:
            # Move the last value to the index being removed
            self.vals[index_to_remove] = last_val
            self.indices[last_val].discard(len(self.vals) - 1)
            self.indices[last_val].add(index_to_remove)

        # Remove the last element
        self.vals.pop()

        # Remove the entry from the dictionary if empty
        if not self.indices[val]:
            del self.indices[val]

        return True

    def getRandom(self) -> int:
        """Gets a random element from the collection."""
        return random.choice(self.vals)


# Example usage:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
