#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        sort(nums.begin(), nums.end());
        int res = 0;
        unordered_map<int, int> counter;
        
        for (int num : nums) {
            counter[num]++;
        }
        
        for (int i = nums[0]; i <= nums.back(); i++) {
            int left = lower_bound(nums.begin(), nums.end(), i - k) - nums.begin();
            int right = upper_bound(nums.begin(), nums.end(), i + k) - nums.begin();
            int currentCount = counter.count(i) ? counter[i] : 0;
            res = max(res, min(right - left, currentCount + numOperations));
        }
        
        return res;
    }
};