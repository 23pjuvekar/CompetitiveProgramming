class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        results = []
        for i in range(n - k + 1):
            window = nums[i : i + k]
            frequency_map = Counter(window)
            freq_items_list = []
            for num, count in frequency_map.items():
                freq_items_list.append((num, count))
            freq_items_list.sort(key=lambda item: (item[1], item[0]), reverse=True)
            top_x_elements = set()
            count_added = 0
            for num, _ in freq_items_list:
                if count_added < x:
                    top_x_elements.add(num)
                    count_added += 1
                else:
                    break
            current_window_x_sum = 0
            for num in window:
                if num in top_x_elements:
                    current_window_x_sum += num
            results.append(current_window_x_sum)

        return results
