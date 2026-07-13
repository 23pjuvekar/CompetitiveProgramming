class Solution {
public:
    int maxDistinct(string s) {
        std::set<char> mySet;

        for (char c : s) {
            mySet.insert(c);
        }
        return mySet.size();
    }
};
