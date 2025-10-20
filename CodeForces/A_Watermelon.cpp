#include <iostream>
using namespace std;

void solve() {
    int x;
    cin >> x;
    if (x > 2 and x % 2 == 0) {
        cout << "YES";
    } else {
        cout << "NO";
    }
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