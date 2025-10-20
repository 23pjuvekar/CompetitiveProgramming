#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {

        int res = 0;
            for (auto op : operations) {
                if (op.substr(0, 2) == "--" or op.substr(1, 3) == "--") {
                res -= 1;
            } else {
                res += 1;
            }
        }
        return res;
    }
};