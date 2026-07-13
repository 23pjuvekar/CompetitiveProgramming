class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        int res = 0;
        int curr = 0;
        for (int i = 0; i < nums.size(); i++){
            curr += nums[i];
            if (curr == 0) {
                res += 1;
            }
        }
        return res;
    }
};
