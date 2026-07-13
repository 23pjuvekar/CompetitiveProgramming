# Create a hashmap
# Create an array of arrays of length k + 1
# Go through array and add number to hashmap with key being number and the value being the count
# Add the value from hashmap into array, where index is the count it appears, and the array inside it is just the values that have that count
# Go from back of array and add elements till k elements is hit
# Return that value

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = []

        for number, counter in count.items():
            freq.append([counter, number])
        
        freq.sort(reverse=True)

        res = []
        for item in freq:
            res.append(item[1])
            if len(res) == k:
                return res
        
        return res
