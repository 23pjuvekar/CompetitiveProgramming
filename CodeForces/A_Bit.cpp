#include <iostream>
using namespace std;

void solve() {
    int n;
    cin >> n;
    int res = 0;
    for (int i = 0; i < n; i++) {
        string op;
        cin >> op;
        if (op == "++X" || op == "X++") {
            res += 1;
        } else {
            res -= 1;
        }
    }
    cout << res << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    //cin >> tc;
    for (int t = 1; t <= tc; t++) {
        //cout << "Case #" << t << ": ";
        solve();
    }
}
