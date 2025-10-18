#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map;
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