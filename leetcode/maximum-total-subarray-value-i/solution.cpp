class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        long long max_element = *std::max_element(nums.begin(), nums.end());
        long long min_element = *std::min_element(nums.begin(), nums.end());
        return k * (max_element - min_element);
    }
};
