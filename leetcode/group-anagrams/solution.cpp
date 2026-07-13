class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, int> mp;
        vector<vector<string>> res;
        for (auto s : strs) {
            string t = s;
            sort(t.begin(), t.end());
            if (mp.find(t) == mp.end()) {
                mp[t] = res.size();
                res.push_back({});
            }
            res[mp[t]].push_back(s);
        }
        return res;


        
    }
};
