#include <iostream>
using namespace std;

void solve() {
    string word;
    cin >> word;
    if (word.length() > 10) {
        cout << word[0] << word.length() - 2 << word[word.length() - 1] << endl;
    } else {
        cout << word << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        //cout << "Case #" << t << ": ";
        solve();
    }
}
