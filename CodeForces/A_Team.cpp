#include <iostream>
using namespace std;

void solve() {
    int n;
    cin >> n;
    int count = 0;
    for (int i = 0; i < n; i ++) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a + b + c >= 2) {
            count += 1;
        }
    }
    cout << count << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    //cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}
