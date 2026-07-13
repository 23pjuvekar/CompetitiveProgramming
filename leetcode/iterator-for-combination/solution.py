class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combos = []
        self.index = 0
        self._generate(characters, combinationLength, 0, "")

    def _generate(self, chars: str, k: int, start: int, current: str):
        if len(current) == k:
            self.combos.append(current)
            return
        for i in range(start, len(chars)):
            self._generate(chars, k, i + 1, current + chars[i])

    def next(self) -> str:
        result = self.combos[self.index]
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combos)
