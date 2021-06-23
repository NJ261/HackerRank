//
// Created by NJadeja on 2021-06-23.
//

#include <iostream>
#include <vector>

using namespace std;

vector<int> rotateLeft(int d, vector<int> arr) {

    int size = arr.size();
    int value = d % size;
    if (value == 0)
    {
        return arr;
    }

    for (int i=0; i<value; i++)
    {
        arr.push_back(arr[i]);
    }
    arr.erase(arr.begin(), arr.begin()+value);

    return arr;
}


int main()
{
    vector<int> v = {1, 2, 3, 4, 5};
    int rotation = 4;

    vector<int> result = rotateLeft(rotation, v);
    for (int i = 0; i < result.size(); ++i) {
        cout << result[i] << " ";
    }

    return 0;
}
