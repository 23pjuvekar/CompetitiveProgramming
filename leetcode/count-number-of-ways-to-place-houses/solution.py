class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10**9 + 7

        ways_ending_empty = 1
        ways_ending_house = 1

        ways_one_side = ways_ending_empty + ways_ending_house

        for _ in range(2, n + 1):
            ways_ending_house = ways_ending_empty
            ways_ending_empty = ways_one_side
            ways_one_side = (ways_ending_house + ways_ending_empty) % MOD

        return (ways_one_side * ways_one_side) % MOD
