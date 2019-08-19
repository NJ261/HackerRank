#include <sstream>
#include <vector>
#include <iostream>
#include <stdlib.h>
using namespace std;

vector<int> parseInts(string str) {
    // Complete this function
    vector<int> data;
    stringstream s(str);

    while(s.good()){
        string word;
        getline( s, word, ',' );
        data.push_back(stoi(word));
    }

    return data;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}

