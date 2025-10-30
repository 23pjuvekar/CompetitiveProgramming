#include <iostream>
#include <map>
using namespace std;

void solve() {
    string username;
    cin >> username;
    int res = 0;
    map<char, int> count;
    for (int i = 0; i < username.size(); i++) {
        count[username[i]] += 1;
        if (count[username[i]] == 1) {
            res += 1;
        } else if (count[username[i] == 2]) {
            res -= 1;
        }
    }
    if (res % 2 == 0) {
        cout << "CHAT WITH HER!" << endl;
    } else {
        cout << "IGNORE HIM!" << endl;
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
