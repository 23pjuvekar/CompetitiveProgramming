class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:

        pref = 0
        total = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            pref = (pref + x) % k
            total += cnt[pref]
            cnt[pref] += 1

        dup = 0
        i = 0
        n = len(nums)
        while i < n:
            v = nums[i]
            j = i
            while j < n and nums[j] == v:
                j += 1
            c = j - i
            g = gcd(v, k)
            step = k // g
            t = c // step
            dup += c * t - step * t * (t + 1) // 2
            i = j

        return total - dup
        
        
        """
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        seen = set()

        P = 31
        M = 10**9 + 7
        
        for i in range(n):
            h = 0
            p_pow = 1
            for j in range(i, n):
                h = (h + (nums[j] + 1) * p_pow) % M
                p_pow = (p_pow * P) % M
                subarray_sum = prefix[j+1] - prefix[i]
                if subarray_sum % k == 0:
                    seen.add(h)
        
        return len(seen)
        """

        """
        n = len(nums)
        total_distinct_count = 0
        prefix_sum = 0

        counts = defaultdict(int)
        counts[0] = 1

        last_occurrence = {}

        dp = [0] * (n + 1)

        for i in range(n):
            prefix_sum += nums[i]
            current_mod = prefix_sum % k

            dp[i + 1] = counts[current_mod]

            p = last_occurrence.get(nums[i], -1)

            duplicates = 0
            if p != -1:
                duplicates = dp[p + 1]

            total_distinct_count += (dp[i + 1] - duplicates)
            counts[current_mod] += 1
            last_occurrence[nums[i]] = i
        return total_distinct_count
        """
        """
        trie = {}
        res = 0
        last = nums[0]

        for i in range(len(nums)):
            curr_node = trie
            curr_sum = 0]
            for j in range(i, len(nums)):
                num = nums[j]
                curr_sum += num
                if num not in curr_node:
                    curr_node[num] = {}
                curr_node = curr_node[num]
                if curr_sum % k == 0 and "marked" not in curr_node:
                    res += 1
                    curr_node["marked"] = True
        return res
        """
