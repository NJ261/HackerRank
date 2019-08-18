//
// Created by nirav on 8/11/19.
//
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, q;
    cin >> n >> q;

    vector<int> arr[n];
    int temp;
    for (int i = 0; i < n; ++i) {
        cin >> temp;
        for (int j = 0; j < temp; ++j) {
            int temp_j;
            cin >> temp_j;
            arr[i].push_back(temp_j);
        }
    }

    for (int k = 0; k < q; ++k) {
        int i, j;
        cin >> i >> j;
        cout << arr[i][j] <<endl;
    }
    return 0;
}
