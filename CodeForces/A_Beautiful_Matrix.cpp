#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void solve() {
    int val = 0;
    int row = -1;
    int col = -1;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> val;
            if (val == 1) {
                row = i;
                col = j;
            }
        }
    }
    int res = abs(2 - row) + abs(2 - col);
    cout << res << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
