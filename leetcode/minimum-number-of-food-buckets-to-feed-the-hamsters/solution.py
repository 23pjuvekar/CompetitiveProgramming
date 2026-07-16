class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        tiles = list(hamsters)
        for index in range(len(tiles)):
            if tiles[index] != 'H':
                continue
            if index > 0 and tiles[index - 1] == 'B':
                continue
            if index < len(tiles) - 1 and tiles[index + 1] == '.':
                tiles[index + 1] = 'B'
            elif index > 0 and tiles[index - 1] == '.':
                tiles[index - 1] = 'B'
            else:
                return -1
        return tiles.count('B')
