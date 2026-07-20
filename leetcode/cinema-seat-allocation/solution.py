class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeatsByRow = {}
        for row, seat in reservedSeats:
            if row not in reservedSeatsByRow:
                reservedSeatsByRow[row] = set()
            reservedSeatsByRow[row].add(seat)

        totalFamilies = 2 * (n - len(reservedSeatsByRow))

        for row, seatsTaken in reservedSeatsByRow.items():
            leftBlockFree = len(seatsTaken.intersection({2, 3, 4, 5})) == 0
            rightBlockFree = len(seatsTaken.intersection({6, 7, 8, 9})) == 0
            middleBlockFree = len(seatsTaken.intersection({4, 5, 6, 7})) == 0

            if leftBlockFree and rightBlockFree:
                totalFamilies += 2
            elif leftBlockFree or rightBlockFree or middleBlockFree:
                totalFamilies += 1

        return totalFamilies
