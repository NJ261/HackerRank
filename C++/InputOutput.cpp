#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int a[n];
    int temp;

    for (int k = 0; k < n; ++k) {
        std::cin >> temp;
        a[k] = temp;
    }

    for (int j = n-1; j >= 0; --j) {
        cout << a[j] << ' ';
    }

    return 0;
}