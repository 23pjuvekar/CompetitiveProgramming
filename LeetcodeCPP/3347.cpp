#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int res = 0;

        // Target in the array
        unordered_map<int, int> m;
        int l = 0, r = 0;
        for (int x : nums) {
            while (r < n && (long long)nums[r] <= (long long)x + k) {
                m[nums[r]]++;
                r++;
            }
            while (l < n && (long long)nums[l] < (long long)x - k) {
                m[nums[l]]--;
                l++;
            }
            int mx_ops = r - l - m[x];
            res = max(res, min(mx_ops, numOperations) + m[x]);
        }

        // Target not in array
        l = 0;
        for (int r = 0; r < n; r++) {
            // Prevent overflow: compare using long long
            while (l < n && (long long)nums[r] - nums[l] > (long long)2 * k) {
                l++;
            }
            int mx_ops = r - l + 1;
            res = max(res, min(mx_ops, numOperations));
        }

        return res;
    }
};