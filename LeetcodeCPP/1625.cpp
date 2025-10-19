#include <unordered_set>
#include <queue>
#include <string>
using namespace std;

class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int n = s.length();
        b = b % n;
        unordered_set<string> seen;
        queue<string> q;
        q.push(s);
        while (!q.empty()) {
            string curr = q.front();
            q.pop();
            if (seen.count(curr)) {
                continue;
            }
            seen.insert(curr);
            string new_string = curr;
            for (int i = 0; i < n; ++i) {
                if (i % 2 == 1) {
                    new_string[i] = '0' + ( (curr[i] - '0' + a) % 10 );
                }
            }
            q.push(new_string);
            string rotated = curr.substr(n - b) + curr.substr(0, n - b);
            q.push(rotated);
        }

        vector<string> candidates(seen.begin(), seen.end());
        sort(candidates.begin(), candidates.end());
        return candidates[0];
    }
};