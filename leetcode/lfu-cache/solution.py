class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}
        self.key_to_freq = defaultdict(int)
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_frequency(self, key: int):
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_to_freq[key] += 1
        new_freq = self.key_to_freq[key]
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1
        
        self._update_frequency(key)
        return self.key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_value:
            self.key_to_value[key] = value
            self._update_frequency(key)
        else:
            if len(self.key_to_value) >= self.capacity:
                lfu_lru_key = next(iter(self.freq_to_keys[self.min_freq]))
                del self.key_to_value[lfu_lru_key]
                del self.key_to_freq[lfu_lru_key]
                del self.freq_to_keys[self.min_freq][lfu_lru_key]
            self.key_to_value[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
