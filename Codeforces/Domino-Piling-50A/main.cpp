#include <iostream>

using namespace std;

int main() {
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;
    int area = m * n;

    cout << ((area - (area % 2))/2);
}