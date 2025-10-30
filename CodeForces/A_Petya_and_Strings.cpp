#include <iostream>
#include <cctype>
using namespace std;

void solve() {

    string word1;
    string word2;

    cin >> word1;
    cin >> word2;

    for (int i = 0; i < word1.size(); i++) {
        if (tolower(word1[i]) > tolower(word2[i])) {
            cout << 1 << endl;
            return;
        } else if (tolower(word1[i]) < tolower(word2[i])) {
            cout << -1 << endl;
            return;
        }
    }
    cout << 0 << endl;
    return;

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
