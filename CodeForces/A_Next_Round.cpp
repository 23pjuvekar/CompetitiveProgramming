#include <iostream>
#include <vector>
using namespace std;

void solve() {
    int n, k;
    cin >> n;
    cin >> k;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    int cutoff = a[k-1];
    int res = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] >= cutoff && a[i] > 0) {
            res++;
        }
    }
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
