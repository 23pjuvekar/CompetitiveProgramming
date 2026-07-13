class StringIterator:
    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.pos = 0 
        self.current_char = None
        self.current_count = 0
        self._parse_next()

    def _parse_next(self):
        if self.pos >= len(self.compressed):
            self.current_char = None
            self.current_count = 0
            return
        self.current_char = self.compressed[self.pos]
        self.pos += 1
        num_str = ""
        while self.pos < len(self.compressed) and self.compressed[self.pos].isdigit():
            num_str += self.compressed[self.pos]
            self.pos += 1
        self.current_count = int(num_str)
        

    def next(self) -> str:
        if self.current_count == 0:
            return " "
        result = self.current_char
        self.current_count -= 1
        if self.current_count == 0:
            self._parse_next()
        return result
        
    def hasNext(self) -> bool:
        return self.current_count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
