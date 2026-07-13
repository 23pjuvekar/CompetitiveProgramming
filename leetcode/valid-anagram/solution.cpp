class Solution {
public:
    bool isAnagram(string s, string t) {

        std::unordered_map<char, int> map;

        for (auto x : s) {
            map[x] += 1;
        }

        for (auto x : t) {
            map[x] -= 1;
        }

        for (auto x : map) {
            if (x.second != 0) {
                return false;
            }
        }

        return true;



        
        
    }
};
