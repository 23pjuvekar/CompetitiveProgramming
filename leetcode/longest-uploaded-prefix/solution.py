class LUPrefix:
    def __init__(self, n: int):
        self._longest = 0
        self._nums = set()

    def upload(self, video: int) -> None:
        self._nums.add(video)
        while self._longest + 1 in self._nums:
            self._longest += 1

    def longest(self) -> int:
        return self._longest
